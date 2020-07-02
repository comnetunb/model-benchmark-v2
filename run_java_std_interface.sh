#!/bin/bash

DIR="$(dirname "$(realpath "$0")")"
cd "$DIR"

if ! ./check_run.sh
then
  exit 1
fi

cd ./java/JavaToPythonStdInterface

if ! (mvn clean && mvn assembly:assembly)
then
  exit 1
fi

cd "$DIR"



java -jar java/JavaToPythonStdInterface/target/JavaToPythonStdInterface-1.0-SNAPSHOT-jar-with-dependencies.jar STDIN "$(pwd)"/config "$(pwd)"/data/dataset.json "$(pwd)"/data/results "$(pwd)"/python/stdin-interface.py