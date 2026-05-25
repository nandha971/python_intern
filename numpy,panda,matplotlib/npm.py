import numpy as np


print("--- 1. Array Creation & Inspection ---")


arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])


zeros = np.zeros((2, 3))       
ones = np.ones((3, 3))         
identity = np.eye(3)           
arange = np.arange(0, 10, 2)  
linspace = np.linspace(0, 1, 5) 

print(f"2D Array Shape: {arr_2d.shape}")
print(f"2D Array Data Type: {arr_2d.dtype}")
print(f"2D Array Dimensions: {arr_2d.ndim}\n")



print("--- 2. Basic Arithmetic ---")
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Exponentiation (b ** 2): {b ** 2}\n")



print("--- 3. Indexing & Slicing ---")
matrix = np.array([[10, 20, 30], 
                   [40, 50, 60], 
                   [70, 80, 90]])

print(f"Specific Element [1, 2] (Row 1, Col 2): {matrix[1, 2]}")
print(f"First Row: {matrix[0, :]}")
print(f"Last Column: {matrix[:, -1]}")
print(f"Sub-matrix (Top-left 2x2):\n{matrix[0:2, 0:2]}")


bool_filter = matrix > 50
print(f"\nElements greater than 50: {matrix[bool_filter]}\n")



print("--- 4. Aggregation & Statistics ---")
data = np.array([[1, 2], [3, 4]])

print(f"Sum of all elements: {data.sum()}")
print(f"Sum across rows (axis=0): {data.sum(axis=0)}")
print(f"Sum across columns (axis=1): {data.sum(axis=1)}")
print(f"Mean (Average): {data.mean()}")
print(f"Standard Deviation: {data.std()}")
print(f"Min/Max: {data.min()} / {data.max()}\n")



print("--- 5. Shape & Matrix Operations ---")
flat_arr = np.array([1, 2, 3, 4, 5, 6])


reshaped = flat_arr.reshape((2, 3))
print(f"Reshaped to 2x3:\n{reshaped}")


print(f"Transposed Matrix:\n{reshaped.T}")


mat_A = np.array([[1, 2], [3, 4]])
mat_B = np.array([[2, 0], [1, 2]])
dot_product = np.dot(mat_A, mat_B)  
print(f"Matrix Dot Product:\n{dot_product}\n")



print("--- 6. Random Numbers ---")

rand_floats = np.random.rand(2, 2) 

rand_ints = np.random.randint(1, 100, size=(5,))

print(f"Random Floats (2x2):\n{rand_floats}")
print(f"Random Integers: {rand_ints}")