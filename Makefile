
PYTHON = python3
PYLINT = $(PYTHON) -m pylint
RUFF = ruff
PYSIDE_UIC = pyside6-uic
MYPY = $(PYTHON) -m mypy

.DELETE_ON_ERROR:

help:                #|# Show this help.
	@echo
	@echo MAIN TARGETS:
	@echo
	@fgrep -h "#|#" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/#|#//'
	@echo

.PHONY: help lint typecheck ruff docker-image-build regenerate-qt regenerate-spec build-linux-exe build-exe

install-dev-deps:    #|# Install developer deps (pylint, ruff, type hints, etc)
	UV_LINK_MODE=copy uv pip install --group dev

install-local:       #|# Perform an "editable" install into venv
	UV_LINK_MODE=copy uv pip install --editable .

lint:                #|# Run pylint
	$(PYLINT) scripts/*py yt_dlp_gui

typecheck:           #|# Run mypy
	$(MYPY) scripts/*py src

ruff:                #|# Run ruff check
	FORCE_COLOR=1 $(RUFF) check .


####
##  qt UI regeneration

%_ui.py: %.ui
	$(PYSIDE_UIC) --from-imports $< -o $@

QT_UI_FILES := $(wildcard src/yt_dlp_gui/ui/*.ui)
PY_UI_FILES := $(QT_UI_FILES:.ui=_ui.py)

$(foreach file,$(PY_UI_FILES),$(eval $(file):))


regenerate-qt:       #|# regenerate Qt UI files
regenerate-qt: $(PY_UI_FILES)
	@echo "Regenerating Qt UI files..."

####
## pyinstaller args

# "--onedir" and "--onfile" are the main executable types
# "--icon" is apparently a no-op except on windows (?).
# "--log-level" is the _build_ log-level
# "--debug=all" causes the app to emit log messages when
#       modules are loaded, unloaded, etc.
# "--collect-all" collects data, code, etc. from the package
# add "--noconsole" to get an exe which doesn't spawn a console

PYINSTALLER_EXE_TYPE = --onedir
PYINSTALLER_ARGS = \
			$(PYINSTALLER_EXE_TYPE) \
			--name=yt-dlp-gui \
			--icon ./src/yt_dlp_gui/ui/assets/yt-dlp-gui.ico \
			--log-level DEBUG \
			--collect-all yt_dlp_gui \
			--copy-metadata yt_dlp_gui \
			--add-data "src/yt_dlp_gui/data/sample_config.toml:yt_dlp_gui/data" \
			--noupx

#			--debug=all

# pyi-makespec just generates the .spec file;
# set this to `pyinstaller` to do a build, as well.
PYINSTALLER_GEN_CMD = pyi-makespec 

regenerate-spec:     #|# regenerate pyinstaller .spec file
	@echo "Regenerating pyinstaller .spec file..."
	uv run $(PYINSTALLER_GEN_CMD) --onedir --name=yt-dlp-gui $(PYINSTALLER_ARGS) scripts/run.py

# On linux, we need to build our pyinstaller exe with an old-ish GNU libc
# which will be widely compatible - so we do our build in a Debian-based
# docker image.

docker-image-build:  #|# Build docker image for linux
	@echo "Building docker image..."
	docker build --progress=plain -t yt-dlp-gui .

build-linux-exe:     #|# build portable Linux executable
	@echo "Building Linux executable..."
	uv run scripts/generate_metadata.py
	uv build --sdist
	scripts/deterministic-tgz.sh dist/yt_dlp_gui*tar.gz dist/sdist.tgz
	docker run --rm --entrypoint=sh -v $(PWD)/dist:/dist yt-dlp-gui \
			-c 'set -x && tar -xf /dist/sdist.tgz --strip-components=1 && \
			uv sync --no-dev && \
			. .venv/bin/activate && \
			uv run pyinstaller --clean -y yt-dlp-gui.spec && \
			cp -a dist/* /dist'
	@echo "Built executable is in dist/"

build-exe:           #|# build executable (non-portable if done on Linux)
	@echo "Building non-Linux executable..."
	uv run pyinstaller --clean -y  yt-dlp-gui.spec
	@echo "Built executable is in dist/"

clean:               #|# delete Python build artifacts
	@echo "cleaning..."
	-rm -rf build dist

extra-clean:         #|# also delete generated Qt UI files
extra-clean:
	@echo "extra cleaning..."
	-rm -rf yt_dlp_gui/ui/*_ui.py

run:                 #|# Run the app via a script
	@echo "running via run.py..."
	uv run scripts/run.py


