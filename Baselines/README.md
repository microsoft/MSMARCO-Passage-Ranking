# Duet Baseline
To help the community reproduce our results and get started quickly, we are including a Duet v2 baseline on our leaderboard. The details of this model can be found in the following paper: https://arxiv.org/abs/1903.07666.

For the Duet v1 model, please see: https://arxiv.org/pdf/1610.08136.pdf and https://arxiv.org/pdf/1705.04803.pdf.

## Requirements
Python 3.5, CUDA 9.0, Pytorch, numpy, jupyter

## Setup
The Duet v2 code is mostly self-contained.
It requires two extra data files, that are not part of the official MS MARCO dataset but are included with the code.

### Vocabulary file
The vocabulary file contains terms from the passage collection whose document frequency is above a certain threshold.
The code references "word-vocab-small.tsv" which contains 71,486 terms from the MS MARCO passage collection.

### Inverse document frequency file
This file contains terms and their corresponding inverse document frequency (IDF) as computed according to the specification in the [paper](https://arxiv.org/abs/1903.07666).

**Important**: The file "idfnew.norm.tsv" only contains terms from queries in MS MARCO train/dev/eval sets.
This is because Duet v2 only needs IDF values corresponding to the terms in the query.
This is not a general purpose IDF dataset for MS MARCO.
If you need one, please make sure to generate one directly from the MS MARCO data.

## Citation
Please cite the following papers, if you use the Duet model in your research.

**Duet v2**
```
@article{mitra2019updated,
  title={An Updated Duet Model for Passage Re-ranking},
  author={Mitra, Bhaskar and Craswell, Nick},
  journal={arXiv preprint arXiv:1903.07666},
  year={2019}
}
```

**Duet v1**
```
@inproceedings{mitra2017learning,
  title={Learning to match using local and distributed representations of text for web search},
  author={Mitra, Bhaskar and Diaz, Fernando and Craswell, Nick},
  booktitle={Proceedings of the 26th International Conference on World Wide Web},
  pages={1291--1299},
  year={2017},
  organization={International World Wide Web Conferences Steering Committee}
}
```

**Duet v1 on TREC CAR**
```
@inproceedings{nanni2017benchmark,
  title={Benchmark for complex answer retrieval},
  author={Nanni, Federico and Mitra, Bhaskar and Magnusson, Matt and Dietz, Laura},
  booktitle={Proceedings of the ACM SIGIR international conference on theory of information retrieval},
  pages={293--296},
  year={2017},
  organization={ACM}
}
```
