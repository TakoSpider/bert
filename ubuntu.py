import fire
import os
reflect = {
    '娱乐': 'news_entertainment', '体育': 'news_sports', '财经': 'news_finance', '房产': 'news_house',
    '汽车': 'news_car', '教育': 'news_edu', '科技': 'news_tech', '军事': 'news_military', '游戏': 'news_game', '其他': 'news_other'
}
files = {
    "data{}train.tsv".format(os.sep): ["data_full{}train.tsv".format(os.sep), 1],
    "data{}test.tsv".format(os.sep): ["data_full{}train.tsv".format(os.sep), 2 / 7],
    "data{}val.tsv".format(os.sep): ["data_full{}val.tsv".format(os.sep), 1 / 7]
}


def main(count):
    for key in files.keys():
        m = {}
        with open(key, "w", encoding="utf-8") as f:
            with open(files[key][0], "r", encoding="utf-8") as f0:
                for line in f0:
                    label = line.split('\t')[0]
                    m.setdefault(label, 0)
                    if m[label] < count * files[key][1]:
                        m[label] += 1
                        f.write(line)


fire.Fire()
