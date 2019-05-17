import pandas as pd
import sys
def main(train_filename, dev_filename, eval_filename):
    train = pd.read_json(train_filename)
    dev = pd.read_json(dev_filename)
    eval = pd.read_json(eval_filename)
    passages = {}
    pid = 0
    for row in train.itterrows():
        for passage in row[1]['passages']:
            if passage['passage_text'] not in passages:
            passages[passage['passage_text']] = pid
            pid += 1
    for row in dev.itterrows():
        for passage in row[1]['passages']:
            if passage['passage_text'] not in passages:
            passages[passage['passage_text']] = pid
            pid += 1
    for row in eval.itterrows():
    for passage in row[1]['passages']:
        if passage['passage_text'] not in passages:
        passages[passage['passage_text']] = pid
        pid += 1
    with open(output_filename, 'w') as w:
    for passage in passages:
        w.write("{}\t{}\n".format(passage, passages[passage])
    print("{} unique passages found".format(str(pid+1)))
    
if __name__ == '__main__':
    if len(sys.argv) != 5:
    print("Usage: get_all_passages.py <train_file> <dev_file> <eval_file> <output_filename>")
    exit(-1)
    else:
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
