import json
import random
import sys


def save_json(path, dataset):
    with open(path, 'w+') as file:
        json.dump(dataset, file)


def generate(seq_count, ranges):
    seq = []
    for i in range(seq_count):
        cur_seq = []
        for r in ranges:
            cur_seq.append(random.uniform(r[0], r[1]))
        seq.append(cur_seq)
    return seq


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc <= 3:
        print('./generator.py out_path count [limits]')
        exit(1)

    path = sys.argv[1]
    count = int(sys.argv[2])
    ranges = []
    for i in range(3, argc):
        ranges.append((0, float(sys.argv[i])))

    data = generate(count, ranges)
    save_json(path, data)
