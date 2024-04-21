import numpy as np
import tensorflow as tf
import torch

sz = (3, 4)

# zeros
print('Zeros:')
print(np.zeros(sz))
print(tf.zeros(sz))
print(torch.zeros(sz))

# ones
print('\nOnes:')
print(np.ones(sz))
print(tf.ones(sz))
print(torch.ones(sz))

# full (np, torch), fill (tf)
print('\nFull (numpy, torch), fill (tensorflow):')
print(np.full(sz, 5))
print(tf.fill(sz, 5))
print(torch.full(sz, 5))