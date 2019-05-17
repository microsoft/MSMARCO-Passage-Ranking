import pandas as pd
import statistics
def remove_empty(a_list):
    b_list = []
    for item in a_list:
        if len(item) > 0:
            b_list.append(item)
    return b_list
train = pd.read_json('train_v2.1.json')
dev = pd.read_json('dev_v2.1.json')
eval = pd.read_json('eval_v2.1_public.json')
question_length, passage_length, words, unique_passages, unique_passages_dev, unique_passages_eval = [], [], {}, {}, {}, {}
data = [train,dev,eval]
for item in data:
    for row in item.iterrows():
        query = row[1]['query']
        question_length.append(len(remove_empty(query.split(' '))))
        for word in query.split(' '):
            words[word] = 0
        for passage in row[1]['passages']:
            passage_text = passage['passage_text']
            for word in passage_text.split(' '):
                words[word] = 0
            if passage['passage_text'] not in unique_passages:
                unique_passages[passage_text] = 0
                passage_length.append(len(remove_empty(passage_text.split(' '))))
with open('top1000.dev.tsv','r') as f:
    for l in f:
        l = l.split('\t')
        unique_passages_dev[l[1]] = 0
with open('top1000.eval.tsv','r') as f:
    for l in f:
        l = l.split('\t')
        unique_passages_eval[l[1]] = 0
print("There are {} unique words".format(len(words)))
print("There are {} unique passages".format(len(unique_passages)))
print("The average question length is {} words with a range {} to {} words".format(statistics.mean(question_length),min(question_length),max(question_length)))
print("The average passage length is {} words with a range {} to {} words".format(statistics.mean(passage_length),min(passage_length),max(passage_length)))
print("Top 1000 dev contains {} unique passages".format(len(unique_passages_dev)))
print("Top 1000 eval contains {} unique passages".format(len(unique_passages_eval)))