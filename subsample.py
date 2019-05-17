import sys
def sub(filename,out, size):
    qids = {}
    with open(filename,'r') as f:
            for l in f:
                    l = l.strip().split('\t')[0]
                    qids[l]= 0
    sample = list(qids)[:size]
    with open(filename,'r') as f:
            with open(out,'w') as w:
                    for l in f:
                            qid = l.strip().split('\t')[0]
                            if qid in sample:
                                    w.write(l)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: subsample.py <input filename> <output filenane> <sample size>")
        exit(-1)
    else:
        sub(sys.argv[1],sys.argv[2],int(sys.argv[3]))