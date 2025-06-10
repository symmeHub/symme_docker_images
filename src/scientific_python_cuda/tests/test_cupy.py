import numpy as np
import cupy as cp

x_gpu = cp.array([1, 1, 1])
l2_gpu = cp.linalg.norm(x_gpu)
# Print the result
print("L2 norm of x_gpu:", l2_gpu)
