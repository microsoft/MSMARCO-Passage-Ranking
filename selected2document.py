import pandas as pd
import json
fullDocumentsFilename = 'fulldocuments.jsonl'
msmarcoQnAFilename = 'fullMSMARCOV2.1.json'
collection = 'collection.tsv'
passage2passageID, docURL2docid = {},{}
with open('collection.tsv','r') as f:
    for l in f:
        l = l.strip().split('\t')
        pid = l[0]
        passageText =  ' '.join(l[1:])
        passage2passageID[passageText] = pid
all = pd.read_json(msmarcoQnAFilename)
i = 0
for row in all.iterrows():
    query = row[1]['query']
    for passage in row[1]['passages']:
            url = passage['url']
            if url not in docURL2docid:
                docURL2docid[url] = i
                i += 1
with open('passageID2DocumentId.tsv','w') as w:
    for row in all.iterrows():
        for passage in row[1]['passages']:
            url = passage['url']
            passageText = passage['passage_text']
            if passageText in passage2passageID and url in docURL2docid:
                w.write('{}\t{}\n'.format(passage2passageID[passageText],docURL2docid[url]))
print("Doneloading QnA")
with open('docID2url.tsv','w') as w:
	for doc in docURL2docid:
		w.write('{}\t{}\n'.format(doc, docURL2docid[doc]))
