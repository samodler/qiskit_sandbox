import numpy as np
from qiskit import __version__


# print(__version__)

#column vectors
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

#operations represented as matrices
M1 = np.array([[1, 1], [0, 0]]) # f(a) = 0
M2 = np.array([[1, 0], [0, 1]]) # f(a) = a

print(f"M1 x ket0 = {M1 @ ket0}")
print(f"M1 x ket1 = {M1 @ ket1}")

print(f"M1 x ket0 = {M1 @ ket0}")
print(f"M2 x ket1 = {M2 @ ket1}")