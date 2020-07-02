#!/bin/bash

cd "$(dirname "$(realpath "$0")")"

# Read length
length=${1:-10000}

# Data folder
mkdir -p data

# Generate dataset
python3 python/utils/generator.py data/dataset.json "$length"