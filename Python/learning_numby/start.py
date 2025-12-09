import numpy as np
import time


# Numpy Array:
arrayDZero = np.array(1)
print(arrayDZero)
print(type(arrayDZero))
print(arrayDZero.dtype)
print(arrayDZero.shape)
print(arrayDZero.ndim)

arrayDOne = np.array([1, 2, 4, 5, 6, 7, 8])
print(arrayDOne)
print(type(arrayDOne))
print(arrayDOne.dtype)
print(arrayDOne.shape)
print(arrayDOne.ndim)

arrayDTwo = np.array([[1, 2, 4], [6, 7, 8], [9, 10, 11]])
print(arrayDTwo)
print(type(arrayDTwo))
print(arrayDTwo.dtype)
print(arrayDTwo.shape)
print(arrayDTwo.ndim)


array = np.array([1, 2, 3])

print(array * 2)  # [2,4,6]
print(array - 2)  # [-1,0,1]
print(array / 2)  # [0.5,1.0,1.5]
print(array ** 2)  # [1,4,9]

# Benefits of Numpy is faster and more efficient because it uses less memory and do without having to loop

# case one for x to arrays is :
# Caclulate the time

number = 10000000
list = [i for i in range(number)]
start = time.time()
arr1 = list
arr2 = list
result = [x * y for y, x in zip(arr1, arr2)]
end = time.time()
print("python result: ", end - start)  # 0.6891469955444336


start = time.time()
arr1 = np.arange(number)
arr2 = np.arange(number)
result = arr1 * arr2
end = time.time()
print("numpy result: ", end - start)  # 0.122314453125

# the difference between them is very big and can make the software faster than with 60%


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)


arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)


start = time.time()
arr = np.arange(number)
x = np.where(arr == 4)
end = time.time()
print("Numpy time: ", end - start, "result: ", '_'.join(str(i)
      for i in x[0]))  # Numpy time:  0.01854395866394043 result:  4

start = time.time()
arr = list
x = "_".join([str(i) for i, v in enumerate(arr) if v == 4])
end = time.time()
# Python time:  0.39185214042663574 result:  4
print("Python time: ", end - start, "result: ", x)


start = time.time()
arr = list
arr = list.sort()
end = time.time()
print("sorting python result: ", end - start)

start = time.time()
arr = np.arange(number)
arr = np.sort(arr)
end = time.time()
print("sorting numpy result: ", end - start)


arr = np.array([1, 2, 3, 4, 5])

print(arr.sum())    # 15
print(arr.mean())   # 3.0
print(np.linalg.norm(arr))


start = time.time()
arr = list
filtered = [x for x in arr if x % 2 == 0]
end = time.time()
print("filtered python result: ", end - start)

start = time.time()
arr = np.arange(number)
filtered = arr[arr % 2 == 0]
end = time.time()
print("filtered numpy result: ", end - start)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)  # 2 blocks, 3 rows, 2 columns
print("Reshaped array (2,3,2):\n", newarr)


arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)  # splits into 3 arrays
print("Array split into 3 parts:", newarr)
print()


vec = np.random.rand(768)  # single embedding of dimension 768
mat = np.random.randn(100, 768)  # 100 embeddings (100x768)
print("Random vector shape:", vec.shape)
print("Random matrix shape:", mat.shape)


arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2D array:\n", arr)
print("Sum along columns (axis=0):", arr.sum(axis=0))
print("Sum along rows (axis=1):", arr.sum(axis=1))
