#!/bin/bash

cd "$(dirname "$(realpath "$0")")"

if ! ./check_run.sh
then
  exit 1
fi

backend=${1:-cpu}

./run_baseline.sh "$backend"
./run_java_native.sh "$backend"
./run_java_std_interface.sh "$backend"