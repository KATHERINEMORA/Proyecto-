import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--method', type=str, choices=['valid', 'same', 'full'], help='Convolution Method')
args = parser.parse_args()

x = [3, 4, 5, 4, 3, 2, 2, 2, 1, 3, 3, 3]
h = [1, -1, 1]

if args.method == "valid" or args.method == "same" or args.method == "full":
 y = np.convolve(x, h, args.method)
else:
 y = np.convolve(x, h)

print(y)
