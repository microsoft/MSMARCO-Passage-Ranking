import math
import re
import sys

MAX_QUERY_TERMS = 80
MAX_DOC_TERMS = 400
regex_drop_char = re.compile('[^a-z0-9\s]+')
regex_multi_space = re.compile('\s+')

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: makeidf.py <train_triples_filename> <dev_rerank_filename> <eval_rerank_filename> <passage_collections_filename>")
        exit(-1)
    else:
        df = {}
        n = 0
        with open(sys.argv[1], encoding = 'utf-8', mode='r') as reader:
            for line in reader:
                cols = line.split('\t')
                for t in regex_multi_space.sub(' ', regex_drop_char.sub(' ', cols[0].lower())).strip().split()[:MAX_QUERY_TERMS]:
                    df[t] = 0
        with open(sys.argv[2], encoding = 'utf-8', mode='r') as reader:
            for line in reader:
                cols = line.split('\t')
                for t in regex_multi_space.sub(' ', regex_drop_char.sub(' ', cols[2].lower())).strip().split()[:MAX_QUERY_TERMS]:
                    df[t] = 0
        with open(sys.argv[3], encoding = 'utf-8', mode='r') as reader:
            for line in reader:
                cols = line.split('\t')
                for t in regex_multi_space.sub(' ', regex_drop_char.sub(' ', cols[2].lower())).strip().split()[:MAX_QUERY_TERMS]:
                    df[t] = 0
        with open(sys.argv[4], encoding = 'utf-8', mode='r') as reader:
            for line in reader:
                cols = line.split('\t')
                for t in set(regex_multi_space.sub(' ', regex_drop_char.sub(' ', cols[1].lower())).strip().split()[:MAX_DOC_TERMS]):
                    if t in df:
                        df[t] += 1
                n += 1
        with open('idf.tsv', encoding = 'utf-8', mode='w') as writer:
            for k, v in df.items():
                writer.write('{}\t{}\n'.format(k, math.log(n / v) if v > 0 else 0))

        n = 0
        with open(sys.argv[3], encoding = 'utf-8', mode='r') as reader:
            for line in reader:
                n += 1
        denom = math.log(n)
        with open('idf.tsv', encoding = 'utf-8', mode='r') as reader:
            with open('idf.norm.tsv', encoding = 'utf-8', mode='w') as writer:
                for line in reader:
                    cols = line.split('\t')
                    score = float(cols[1])
                    if score > 0:
                        writer.write('{}\t{}\n'.format(cols[0], score / denom))
