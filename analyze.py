#!/usr/bin/python3

import json
import pandas as pd


def read(path):
    with open(path) as json_file:
        return json.load(json_file)


def get_data_frame(info):
    results = []
    for res in info['results']:
        results.append(res['duration'] / 1000)
    return pd.DataFrame(results)[0]


baseline_results = read('./data/results/cpu/baseline.json')
java_native_results = read('./data/results/cpu/java-native.json')
java_python_results = read('./data/results/cpu/java-python-interface.json')
baseline_results_gpu = read('./data/results/gpu/baseline.json')
java_native_results_gpu = read('./data/results/gpu/java-native.json')
java_python_results_gpu = read('./data/results/gpu/java-python-interface.json')

# Baseline

baseline_frame = get_data_frame(baseline_results)
print('############################################################')
print(' Baseline ')
print('############################################################')
print()
print('total:', baseline_frame.size)
print('avg:', baseline_frame.mean(), 'ms')
print('median:', baseline_frame.median(), 'ms')
print('stdev:', baseline_frame.std(), 'ms')
print('min:', baseline_frame.min(), 'ms')
print('max:', baseline_frame.max(), 'ms')
print()

# Java Native

java_native_frame = get_data_frame(java_native_results)
print('############################################################')
print(' Java Native ')
print('############################################################')
print()
print('total:', java_native_frame.size)
print('avg:', java_native_frame.mean(), 'ms')
print('median:', java_native_frame.median(), 'ms')
print('stdev:', java_native_frame.std(), 'ms')
print('min:', java_native_frame.min(), 'ms')
print('max:', java_native_frame.max(), 'ms')
print()

# Java Python Interface

java_python_frame = get_data_frame(java_python_results)
print('############################################################')
print(' Java Python Interface ')
print('############################################################')
print()
print('total:', java_python_frame.size)
print('avg:', java_python_frame.mean(), 'ms')
print('median:', java_python_frame.median(), 'ms')
print('stdev:', java_python_frame.std(), 'ms')
print('min:', java_python_frame.min(), 'ms')
print('max:', java_python_frame.max(), 'ms')
print()

# Baseline GPU

baseline_frame_gpu = get_data_frame(baseline_results_gpu)
print('############################################################')
print(' Baseline ')
print('############################################################')
print()
print('total:', baseline_frame_gpu.size)
print('avg:', baseline_frame_gpu.mean(), 'ms')
print('median:', baseline_frame_gpu.median(), 'ms')
print('stdev:', baseline_frame_gpu.std(), 'ms')
print('min:', baseline_frame_gpu.min(), 'ms')
print('max:', baseline_frame_gpu.max(), 'ms')
print()

# Java Native GPU

java_native_frame_gpu = get_data_frame(java_native_results_gpu)
print('############################################################')
print(' Java Native ')
print('############################################################')
print()
print('total:', java_native_frame_gpu.size)
print('avg:', java_native_frame_gpu.mean(), 'ms')
print('median:', java_native_frame_gpu.median(), 'ms')
print('stdev:', java_native_frame_gpu.std(), 'ms')
print('min:', java_native_frame_gpu.min(), 'ms')
print('max:', java_native_frame_gpu.max(), 'ms')
print()

# Java Python Interface GPU

java_python_frame_gpu = get_data_frame(java_python_results_gpu)
print('############################################################')
print(' Java Python Interface ')
print('############################################################')
print()
print('total:', java_python_frame_gpu.size)
print('avg:', java_python_frame_gpu.mean(), 'ms')
print('median:', java_python_frame_gpu.median(), 'ms')
print('stdev:', java_python_frame_gpu.std(), 'ms')
print('min:', java_python_frame_gpu.min(), 'ms')
print('max:', java_python_frame_gpu.max(), 'ms')
print()
