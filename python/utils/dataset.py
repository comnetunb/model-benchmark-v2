import json
from pathlib import Path


def read_dataset(path):
    with open(path) as json_file:
        return json.load(json_file)


def write_results(path, name, results):
    cur_path = Path(path).resolve()
    res_path = Path.joinpath(cur_path, name)
    with open(res_path, 'w+') as json_file:
        json.dump(results, json_file)
