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


def run(path, count, ranges):
    data = generate(count, ranges)

    inp = {
        'warm_up': generate(count // 10, ranges),
        'data': generate(count, ranges),
    }
    save_json(path, inp)


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 3:
        print('./generator.py out_path count')
        exit(1)

    path = sys.argv[1]
    count = int(sys.argv[2])
    ranges = [(12, 450), (0, 5), (1, 8), (3, 70),
              (250, 6900), (0, 201), (0, 49)]

    run(path, count, ranges)
