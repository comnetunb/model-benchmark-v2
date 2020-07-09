#!/bin/bash

cd "$(dirname "$(realpath "$0")")"

if ! ./check_run.sh
then
  exit 1
fi

####################################################################################################

echo 'Sourcing conda shell.bash hook'
eval "$(conda shell.bash hook)"

####################################################################################################

backend=${1:-cpu}

if [ $backend = 'cpu' ]; then
  echo 'Activating conda environment with CPU Backend'
  conda activate model-benchmark-v2
else
  echo 'Activating conda environment with GPU Backend'
  conda activate model-benchmark-v2.1
fi

####################################################################################################

python3 python/baseline.py ./config ./data/dataset.json ./data/results
