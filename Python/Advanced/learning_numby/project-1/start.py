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
