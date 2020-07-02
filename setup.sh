#!/bin/bash

####################################################################################################

echo 'Checking if all config files exist'

FILE=data/dataset.json
if [ ! -f "$FILE" ]; then
    echo "$FILE does not exist."
fi

FILE=config/model.sav
if [ ! -f "$FILE" ]; then
    echo "$FILE does not exist."
fi

FILE=config/scaler.pkl
if [ ! -f "$FILE" ]; then
    echo "$FILE does not exist."
fi

####################################################################################################

echo 'Checking if conda is installed'

if ! conda info &> /dev/null
then
    echo "Conda is not installed, installing it..."
    curl -s -L "https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-Linux-x86_64.sh" | md5sum -c <(echo "751786b92c00b1aeae3f017b781018df  -") | bash
fi

####################################################################################################

echo 'Sourcing conda shell.bash hook'
eval "$(conda shell.bash hook)"

####################################################################################################

echo 'Creating conda environment'
conda env create -f python/environment.yml --force > /dev/null

####################################################################################################

echo 'Activating conda environment'
conda activate model-benchmark-v2

####################################################################################################