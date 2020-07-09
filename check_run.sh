#!/bin/bash

cd "$(dirname "$(realpath "$0")")"

####################################################################################################

FILE=data/dataset.json
if [ ! -f "$FILE" ]; then
    echo "Run ./generate.sh [length]"
    exit 1
fi

####################################################################################################

mkdir -p ./data/results/cpu
mkdir -p ./data/results/gpu