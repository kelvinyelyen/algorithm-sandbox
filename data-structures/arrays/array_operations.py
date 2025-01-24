# Import necessary modules
import array
import numpy as np

# --------------------------
# Section 1: Using Python Lists
# --------------------------
print("\n--- Python Lists ---")
# Creating a list (dynamic array)
list_array = [1, 2, 3, 4, 5]
print("List:", list_array)

# Accessing elements
print("First element:", list_array[0])
print("Last element:", list_array[-1])

# Modifying elements
list_array[2] = 10
print("After modification:", list_array)

# Adding elements
list_array.append(6)  # Append to the end
list_array.insert(2, 7)  # Insert at index 2
print("After adding elements:", list_array)

# Removing elements
if 3 in list_array:
    list_array.remove(3)  # Remove by value
else:
    print("Value 3 not found in list_array.")

if len(list_array) > 2:
    removed_element = list_array.pop(2)  # Remove by index
    print("Removed element:", removed_element)
else:
    print("Index 2 is out of range.")
print("After removing elements:", list_array)

# Iterating through the list
print("Iterating through list:")
for element in list_array:
    print(element, end=" ")
print()

# Slicing
sub_list = list_array[1:4]  # Subset from index 1 to 3
print("Sliced list:", sub_list)

# Sorting
list_array.sort()
print("Sorted list:", list_array)

list_array.sort(reverse=True)
print("Reverse sorted list:", list_array)

# --------------------------
# Section 2: Using the `array` Module
# --------------------------
print("\n--- Array Module ---")
# Creating an array (homogeneous)
arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' = integer type
print("Array:", arr)

# Accessing elements
print("First element:", arr[0])
print("Last element:", arr[-1])

# Modifying elements
arr[2] = 10
print("After modification:", arr)

# Adding elements
arr.append(6)
print("After append:", arr)

# Removing elements
if 3 in arr:
    arr.remove(3)
else:
    print("Value 3 not found in array.")

if len(arr) > 2:
    removed_element = arr.pop(2)
    print("Removed element:", removed_element)
else:
    print("Index 2 is out of range.")
print("After removing elements:", arr)

# Iterating through the array
print("Iterating through array:")
for element in arr:
    print(element, end=" ")
print()

# --------------------------
# Section 3: Using NumPy Arrays
# --------------------------
print("\n--- NumPy Arrays ---")
# Creating a NumPy array
np_array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", np_array)

# Element-wise operations
print("Array + 2:", np_array + 2)
print("Array * 3:", np_array * 3)

# Advanced operations
print("Mean:", np_array.mean())
print("Sum:", np_array.sum())
print("Max:", np_array.max())

# Reshaping an array
reshaped_array = np_array.reshape(1, -1)
print("Reshaped Array (1x5):", reshaped_array)

# Adding elements (NumPy)
np_array = np.append(np_array, [6, 7])
print("After append:", np_array)

# Slicing
sub_np_array = np_array[1:4]
print("Sliced NumPy Array:", sub_np_array)

# Sorting
sorted_np_array = np.sort(np_array)
print("Sorted NumPy Array:", sorted_np_array)

# --------------------------
# Section 4: 3x3 Arrays and Matrices
# --------------------------
print("\n--- 3x3 Arrays and Matrices ---")

# Creating a 3x3 list-based array
matrix_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("3x3 Matrix (List-based):")
for row in matrix_list:
    print(row)

# Accessing elements
print("Element at (1,1):", matrix_list[1][1])

# Creating a 3x3 NumPy array
matrix_np = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("\n3x3 Matrix (NumPy):")
print(matrix_np)

# Transpose of the matrix
transpose_np = matrix_np.T
print("Transpose of NumPy Matrix:")
print(transpose_np)

# Matrix multiplication
identity_matrix = np.eye(3)
product_matrix = np.matmul(matrix_np, identity_matrix)
print("Matrix multiplied by identity matrix:")
print(product_matrix)

# Determinant
det_matrix = np.linalg.det(matrix_np)
print("Determinant of 3x3 Matrix:", det_matrix)

# Inverse
if det_matrix != 0:
    inverse_matrix = np.linalg.inv(matrix_np)
    print("Inverse of 3x3 Matrix:")
    print(inverse_matrix)
else:
    print("Matrix is singular and cannot be inverted.")

# --------------------------
# Summary
# --------------------------
print("\n--- Summary ---")
print("Python Lists: Flexible and easy for general use.")
print("Array Module: Type-specific and lightweight.")
print("NumPy Arrays: Best for numerical computations and large datasets.")
print("3x3 Matrices: NumPy provides efficient matrix operations.")
# --------------------------
