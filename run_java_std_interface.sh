#!/bin/bash

DIR="$(dirname "$(realpath "$0")")"
cd "$DIR"

if ! ./check_run.sh
then
  exit 1
fi


####################################################################################################

FILE=java/target/Java-1.0-SNAPSHOT-jar-with-dependencies.jar
if [ ! -f "$FILE" ]; then
  cd ./java
  if ! (mvn clean && mvn assembly:assembly)
  then
    exit 1
  fi
fi

####################################################################################################

cd "$DIR"

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

java -jar "$FILE" STDIN "$(pwd)"/config "$(pwd)"/data/dataset.json "$(pwd)"/data/results/"$backend" "$(pwd)"/python/stdin-interface.py