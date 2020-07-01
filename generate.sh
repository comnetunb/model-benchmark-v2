#!/bin/bash

# Read length
length=${1:-10000}

# Data folder
mkdir -p data

# Generate dataset
python3 python/utils/generator.py data/dataset.json "$length" 10 10 10 10 10 10 10