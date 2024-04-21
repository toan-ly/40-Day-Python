import numpy as np
import tensorflow as tf
import torch

# 1
ls = list(range(1, 5))
ls_np = np.array(ls)
ls_tf = tf.constant(ls)
ls_torch = torch.tensor(ls)

print(ls_np)
print(ls_tf)
print(ls_torch)

# 2   
def display(ls_type, ls):
    print()
    print(f'{ls_type}:') 
    print(ls)
    print(f'Shape: {ls.shape}')
    print(f'Dtype: {ls.dtype}')
    print(f'Type: {type(ls)}')
    if not isinstance(ls, np.ndarray):
        print(f'Device: {ls.device}')

ls_2d_np = np.arange(1, 13).reshape(3, 4)
display('2D Numpy', ls_2d_np)

ls_2d_tf = tf.constant(ls_2d_np)
display('2D Tensorflow', ls_2d_tf)

ls_2d_torch = torch.tensor(ls_2d_np)
display('2D Torch', ls_2d_torch)


