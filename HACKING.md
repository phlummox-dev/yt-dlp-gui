
Notes on internals, developer setup, and design decisions.

## setup

Run `scripts/install-hooks.sh` to set up some commit hooks that protect the package
`__init__.py` file, containing app metadata. It generally shouldn't be edited, just
overwritten by CI/CD scripts at build time.

## CI/CD pipelines

We build executables using pyinstaller - mostly for the benefit of Windows users who don't have
Python installed.

Other users (MacOS, Linux) should generally be able to install Python easily enough, but we
supply executables anyway. (TODO: Probably an AppImage or flatpak would be better.)

For linux - to create a portable, packed executable with pyinstaller, we need a low version of
GNU libc, so it's compatible with most users' platforms; but we also want a fairly recent version
of Python.

The GNU libc in GitHub's Ubuntu runners are all too recent, so we build in a docker image based on
Debian bullseye (uses glibc 2.31, released Feb 2020).




