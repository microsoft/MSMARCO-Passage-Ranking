import sys
import json
import time
import re
from bert_serving.client import BertClient
regex_drop_char = re.compile('[^a-z0-9\\s]+')
regex_multi_space= re.compile('\\s+')
def loadPassages(filename):
    passages = {}
    with open(filename,'r') as f:
        for l in f:
            l = l.strip().split('\t')
            i = int(l[0])
            passages[i] = regex_multi_space.sub(' ', regex_drop_char.sub(' ', ' '.join(l[1:]).lower())).strip()
    return passages
def process(passageIDs, response):
    output = ''
    for i in range(len(passageIDs)):
        output += "{}\t".format(passageIDs[i])
        for j in range(len(response[i])):
            output += "{} ".format(response[i][j])
        output += "\n"
    return output
def getVectors(passages, filename):
    i = 1
    bc = BertClient()
    passage = 'In June 1942, the United States Army Corps of Engineersbegan the Manhattan Project- The secret name for the 2 atomic bombs.'
    print("Testing bc\nTesting passages:{}\nVector:{}".format(passage, bc.encode([passage])[0]))
    passagePack = []
    passageIDs = []
    packSize = 100
    with open(filename,'w') as w:
        for passageID in passages:
            if i % 100 == 0:
                print('{} vectors retrieved'.format((i-1)*packSize))
            if len(passagePack) == packSize:
                response = bc.encode(passagePack)
                w.write(process(passageIDs, response))
                passageIDs = []
                passagePack = []
                i += 1
            passageIDs.append(passageID)
            passagePack.append(passages[passageID])
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: generatePassagesEmbeddingsBERT.py <passagesFile> <outputfile>')
        exit(-1)
    else:
        passages = loadPassages(sys.argv[1])
        print("{} passages loaded".format(len(passages)))
        getVectors(passages, sys.argv[2])
