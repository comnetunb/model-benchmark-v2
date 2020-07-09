#!/bin/bash

DIR="$(dirname "$(realpath "$0")")"
cd "$DIR"

if ! ./check_run.sh
then
  exit 1
fi

####################################################################################################

backend=${1:-cpu}

if [ $backend = 'cpu' ]; then
  echo 'Getting POM of CPU backend'
  cp -f java/pom-cpu.xml java/pom.xml
else
  echo 'Getting POM of GPU backend'
  cp -f java/pom-gpu.xml java/pom.xml
fi

####################################################################################################

FILE=java/target/Java-1.0-SNAPSHOT-bin.jar
if [ ! -f "$FILE" ]; then
  cd ./java
  if ! (mvn clean && mvn package)
  then
    exit 1
  fi
fi

####################################################################################################

cd "$DIR"

java -jar "$FILE" NATIVE "$(pwd)"/config "$(pwd)"/data/dataset.json "$(pwd)"/data/results/"$backend"