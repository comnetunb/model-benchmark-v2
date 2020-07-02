#!/bin/bash

if ! ./check_run.sh
then
  exit 1
fi

./run_baseline.sh