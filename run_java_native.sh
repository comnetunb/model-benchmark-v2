#!/bin/bash

DIR="$(dirname "$(realpath "$0")")"
cd "$DIR"

if ! ./check_run.sh
then
  exit 1
fi

cd ./java

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

java -jar java/target/Java-1.0-SNAPSHOT-jar-with-dependencies.jar NATIVE "$(pwd)"/config "$(pwd)"/data/dataset.json "$(pwd)"/data/results