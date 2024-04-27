import numpy as np

# Define matrix A and vector B
A = np.array([[7068, 671, 976, 4399, 974],
              [77, 4341, 195, 9424, 9205],
              [7510, 4546, 7116, 4780, 8395],
              [356, 6125, 3120, 7116, 5741],
              [8669, 1245, 5826, 8322, 5886]])

B = np.array([16642437, 66990465, 64290234, 52223804, 54123553])

# Calculate the inverse of matrix A
A_inv = np.linalg.inv(A)

# Solve for X
X = np.dot(A_inv, B)

print(X)
