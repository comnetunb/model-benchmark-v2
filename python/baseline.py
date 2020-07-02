import sys
import time
from utils.dataset import read_dataset, write_results
from classifier.classifier import Classifier


def classify(classifier, data):
    start = time.time()
    res = classifier.classify(data)
    end = time.time()

    nanoseconds = int((end - start) * 1e6)
    return (res, nanoseconds)


def run(config_path, dataset_path, output_path):

    dataset = read_dataset(dataset_path)
    classifier = Classifier(config_path)

    run_info = {}

    run_info['name'] = 'Baseline Run - Hot loop in Python implementation'

    run_info['results'] = []
    for seq in dataset:
        instance = {}
        result, duration = classify(classifier, seq)
        instance['input'] = seq
        instance['output'] = result
        instance['duration'] = duration
        run_info['results'].append(instance)

    write_results(output_path, 'baseline.json', run_info)


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 4:
        print('./baseline.py config_path dataset_path output_path')
        exit(1)

    run(sys.argv[1], sys.argv[2], sys.argv[3])
