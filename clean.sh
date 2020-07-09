#!/bin/sh


DIR="$(dirname "$(realpath "$0")")"
cd "$DIR"

if ! ./check_run.sh
then
  exit 1
fi

rm -rf ./java/target