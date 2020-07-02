#!/bin/bash

if ! ./check_run.sh
then
  exit 1
fi

####################################################################################################

echo 'Sourcing conda shell.bash hook'
eval "$(conda shell.bash hook)"

####################################################################################################

echo 'Activating conda environment'
conda activate model-benchmark-v2

####################################################################################################

python3 python/baseline.py ./config ./data/dataset.json ./data/results