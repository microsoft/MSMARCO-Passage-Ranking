wget https://msmarco.blob.core.windows.net/msmarcoranking/collectionandqueries.tar.gz
wget https://msmarco.blob.core.windows.net/msmarcoranking/fulldocuments.jsonl.gz
wget https://msmarco.blob.core.windows.net/msmarcoranking/triples.train.small.tar.gz
wget https://msmarco.blob.core.windows.net/msmarcoranking/triples.train.full.tar.gz
wget https://msmarco.blob.core.windows.net/msmarcoranking/top1000.dev.tar.gz
wget https://msmarco.blob.core.windows.net/msmarcoranking/top1000.eval.tar.gz
wget https://msmarco.blob.core.windows.net/msmarco/train_v2.1.json.gz
wget https://msmarco.blob.core.windows.net/msmarco/dev_v2.1.json.gz
wget https://msmarco.blob.core.windows.net/msmarco/eval_v2.1_public.json.gz
gunzip eval_v2.1_public.json.gz
gunzip fulldocuments.jsonl.gz
gunzip dev_v2.1.json.gz
gunzip train_v2.1.json.gz
tar -xzvf top1000.eval.tar.gz
tar -xzvf top1000.dev.tar.gz
tar -xzvf triples.train.small.tar.gz
tar -xzvf triples.train.full.tar.gz
tar -xzvf queries.tar.gz
tar -xzvf collection.tar.gz
rm *.gz
