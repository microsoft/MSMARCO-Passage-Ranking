#!/bin/bash
# File Name : run.sh
# Command line: /ms_marco_metrics$ ./run.sh <path to candidate file>
# Creation Date : Mar-20-2019
# Last Modified : Mar-20-2019
# Authors : Daniel Campos <dacamp@microsoft.com>
python3 ms_marco_eval.py $1 $2
