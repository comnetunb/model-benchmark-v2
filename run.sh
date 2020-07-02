#!/bin/bash

cd "$(dirname "$(realpath "$0")")"

if ! ./check_run.sh
then
  exit 1
fi

./run_baseline.sh
./run_java_native.sh
./run_java_std_interface.sh