import numpy as np
from scipy import signal
import scipy.ndimage

a = np.array([[0,  0,  0,  0,  0],
              [0,  0,  0,  0,  0],
              [0,  0,  1,  0,  0],
              [0,  0,  0,  0,  0],
              [0,  0,  0,  0,  0],])

convolution_filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# z = signal.convolve2d(a, convolution_filter)
# print(z)

filter = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# filtered_array = scipy.ndimage.convolve(a, filter)
filtered_array = scipy.ndimage.correlate(a, filter, mode="nearest")  # mode: ['constant', 'nearest] .transpose()

print(filtered_array)
