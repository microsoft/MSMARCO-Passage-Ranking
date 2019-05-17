import pandas as pd
import sys

relevant_train = {}
relevant_dev = {}
relevant_eval = {}
eval = pd.read_json('eval_v2.1_hidden.json')
train = pd.read_json('train_v2.1.json')
dev = pd.read_json('dev_v2.1.json')

for row in train.iterrows():
    query_id = row[1]['query_id']
    for passage in row[1]['passages']:
        if passage['is_selected'] == 1:
            relevant_train[(query_id,passage['passage_text'])] = 0

print(len(relevant_train))

for row in dev.iterrows():
    query_id = row[1]['query_id']
    for passage in row[1]['passages']:
        if passage['is_selected'] == 1:
            relevant_dev[(query_id,passage['passage_text'])] = 0

print(len(relevant_dev))

for row in eval.iterrows():
    query_id = row[1]['query_id']
    for passage in row[1]['passages']:
        if passage['is_selected'] == 1:
            relevant_eval[(query_id,passage['passage_text'])] = 0
with open('qrel.eval.tsv','w') as w:
    for item in relevant_eval:
        print(item)
print(len(relevant_eval))

