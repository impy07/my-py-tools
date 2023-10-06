import numpy as np
import math
import sys
import os

if(len(sys.argv) == 1):
    print(f'USAGE: {sys.argv[0]} <File name>');
    sys.exit(-1)

filepath = os.path.abspath(sys.argv[1])
with open(sys.argv[1], 'rb') as fh:

    array = bytearray(fh.read())

    _, counts = np.unique(array, return_counts=True)
    probabilities = counts / len(array)

    shannon_entropy = -np.sum(probabilities * np.log2(probabilities))
    print(shannon_entropy)
