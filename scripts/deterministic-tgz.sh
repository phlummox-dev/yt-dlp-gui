#!/usr/bin/env sh

# make a byte-for-byte reproducible tar.gz file from a non-repro one

if [ "$#" -ne 2 ]; then
  echo >&2 "expected INFILE and OUTFILE"
  exit 1
fi

set -x

infile="$1"
outfile="$2"

set -eu

tmpdir=$(mktemp --directory --tmpdir --suffix=.ytdl)

tar -C "$tmpdir" -xf "$infile"

TAR_ARGS="--format=posix --sort=name --owner=0 --group=0 --numeric-owner --clamp-mtime --pax-option=delete=atime,delete=ctime" 

# shellcheck disable=SC2086
(cd "$tmpdir" && tar -cf - $TAR_ARGS --mtime='@0' yt_dlp_gui*) | gzip --no-name > "$outfile"

rm -rf "$tmpdir"

