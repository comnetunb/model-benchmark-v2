import os
import sys
import pandas as pd
from classifier.classifier import Classifier


def run(config_path):
    classifier = Classifier(config_path)

    sys.stdout.write('READY\n')
    sys.stdout.flush()

    for line in sys.stdin:
        values = [float(elem) for elem in line.split()]
        res = classifier.classify(values)
        sys.stdout.write(f'{res}\n')
        sys.stdout.flush()


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        print('./baseline.py config_path')
        exit(1)

    run(sys.argv[1])
