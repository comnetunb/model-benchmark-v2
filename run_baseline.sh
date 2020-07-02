#!/bin/bash

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

mkdir -p ./data/results

# Generate dataset
python3 python/baseline.py ./config ./data/dataset.json ./data/results