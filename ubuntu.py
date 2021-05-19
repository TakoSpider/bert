import fire
import os

files = {
    "data{}train.tsv".format(os.sep): ["data_full{}train.tsv".format(os.sep), 1],
    "data{}test.tsv".format(os.sep): ["data_full{}train.tsv".format(os.sep), 1 / 7],
    "data{}val.tsv".format(os.sep): ["data_full{}train.tsv".format(os.sep), 1 / 7]
}


def main(count = -1):
    for key in files.keys():
        m = {}
        with open(key, "w", encoding="utf-8") as f:
            with open(files[key][0], "r", encoding="utf-8") as f0:
                for line in f0:
                    label = line.split('\t')[1]
                    m.setdefault(label, 0)
                    if m[label] < count * files[key][1]:
                        m[label] += 1
                        f.write(line)


fire.Fire()
