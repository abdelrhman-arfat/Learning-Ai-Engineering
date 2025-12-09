# To start:

1. setting up venv

```bash
 python -m venv .venv
```

- active in git script is

```bash
source .venv/bin/activate
```

- active on powershell

```bash
.venv\bin\Activate.ps1
```

2. install dep

```bash
pip install numpy
```

# ===========================

# NumPy Practical Reference - Organized for Learning AI / Embeddings

# Each section explains the logic and purpose

# ===========================

```python
import numpy as np
import time
```

# ===========================

# 1️⃣ Creating Arrays (0D, 1D, 2D)

# ===========================

# 0D array = scalar

```python

arrayDZero = np.array(1)
print("0D array:", arrayDZero)
print("Type:", type(arrayDZero))
print("Data type:", arrayDZero.dtype)
print("Shape:", arrayDZero.shape)
print("Number of dimensions:", arrayDZero.ndim)


# 1D array

arrayDOne = np.array([1, 2, 4, 5, 6, 7, 8])
print("1D array:", arrayDOne)
print("Shape:", arrayDOne.shape)
print("Number of dimensions:", arrayDOne.ndim)


# 2D array

arrayDTwo = np.array([[1,2,4],[6,7,8],[9,10,11]])
print("2D array:\n", arrayDTwo)
print("Shape:", arrayDTwo.shape)
print("Number of dimensions:", arrayDTwo.ndim)

```

# ===========================

# 2️⃣ Element-wise Operations

# ===========================

```python
# NumPy arrays allow operations on all elements at once (vectorization)
arr = np.array([1,2,3])
print("Original array:", arr)
print("Multiply by 2:", arr\*2)
print("Subtract 2:", arr-2)
print("Divide by 2:", arr/2)
print("Power 2:", arr\*\*2)

```

# ===========================

# 3️⃣ Performance Comparison Python vs NumPy

# ===========================

```python

number = 10000000
list_data = [i for i in range(number)]

# Python list multiplication (slower)


start = time.time()
arr1 = list_data
arr2 = list_data
result = [x*y for x,y in zip(arr1, arr2)]
end = time.time()
print("Python list multiplication time:", end-start)

# NumPy array multiplication (much faster)


start = time.time()
arr1 = np.arange(number)
arr2 = np.arange(number)
result = arr1 \* arr2
end = time.time()
print("NumPy array multiplication time:", end-start)
```

# ===========================

# 4️⃣ Reshape and Split Arrays

# ===========================

# Reshape a 1D array to 3D

```python

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2) # 2 blocks, 3 rows, 2 columns
print("Reshaped array (2,3,2):\n", newarr)

# Split an array into equal parts


arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3) # splits into 3 arrays
print("Array split into 3 parts:", newarr)

```

# ===========================

# 5️⃣ Find Elements (np.where) vs Python

# ===========================

# NumPy approach

```python

arr = np.arange(number)
start = time.time()
x = np.where(arr==4)
end = time.time()
print("NumPy where time:", end-start)
print("Result index:", '\_'.join(str(i) for i in x[0]))

# Python approach

start = time.time()
x = "\_".join([str(i) for i,v in enumerate(list_data) if v==4])
end = time.time()
print("Python list find time:", end-start)
print("Result index:", x)

```

# ===========================

# 6️⃣ Sorting Arrays

# ===========================

# Python list sort

```python
arr = list_data.copy()
start = time.time()
arr.sort()
end = time.time()
print("Python list sort time:", end-start)

# NumPy sort

arr = np.arange(number)
start = time.time()
np.sort(arr)
end = time.time()
print("NumPy array sort time:", end-start)
```

# ===========================

# 7️⃣ Sum, Mean, Norm

# ===========================

```python
arr = np.array([1,2,3,4,5])
print("Array:", arr)
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Norm (length of vector):", np.linalg.norm(arr))
```

# ===========================

# 8️⃣ Filter Elements (Boolean Indexing)

# ===========================

# Python list filtering

```python
arr = list_data
start = time.time()
filtered = [x for x in arr if x%2==0]
end = time.time()
print("Python filtered even numbers time:", end-start)
# NumPy filtering
arr = np.arange(number)
start = time.time()
filtered = arr[arr%2==0]
end = time.time()
print("NumPy filtered even numbers time:", end-start)

```

embeddings

# ===========================

# 9️⃣ Advanced Slicing and Views vs Copy

# ===========================

```python
arr = np.array([1,2,3,4,5])
view = arr[1:4] # view (modifies original)
view[0] = 99
print("Array after view modification:", arr)

copy = arr[1:4].copy() # copy (does NOT modify original)
copy[0] = 100
print("Array after copy modification:", arr)

```

# ===========================

# 10️⃣ Stacking / Concatenation

# ===========================

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

# Concatenate 1D

print("Concatenate 1D:", np.concatenate([a,b]))

# Horizontal stack (axis=1 for 2D, same as hstack for 1D)

print("Hstack 1D:", np.hstack([a,b]))

# Vertical and Horizontal stacking for 2D

arr1 = np.array([[1,2,3]])
arr2 = np.array([[4,5,6]])
print("Concatenate axis=0 (vertical):\n", np.concatenate([arr1,arr2], axis=0))
print("Vstack:\n", np.vstack([arr1,arr2]))
print("Hstack:\n", np.hstack([arr1,arr2]))

```

# ===========================

# 11️⃣ Random Numbers / Embeddings

# ===========================

```python
# Create random  for AI

vec = np.random.rand(768) # single embedding of dimension 768
mat = np.random.randn(100,768) # 100 embeddings (100x768)
print("Random vector shape:", vec.shape)
print("Random matrix shape:", mat.shape)
```

# ===========================

# 12️⃣ Linear Algebra - Dot Product and Cosine Similarity

# ===========================

```python
a = np.array([1,2,3])
b = np.array([4,5,6])
dot = np.dot(a,b)
norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)
cos_sim = dot / (norm_a\*norm_b)
print("Dot product:", dot)
print("Norm a:", norm_a)
print("Norm b:", norm_b)
print("Cosine similarity:", cos_sim)
```

# ===========================

# 13️⃣ Broadcasting

# ===========================

```python

arr = np.array([1,2,3])
print("Original array:", arr)
print("Add 10 to all elements:", arr+10) # broadcasting
print("Multiply by 2:", arr\*2)

```

# ===========================

# 14️⃣ Axis Operations

# ===========================

```python

arr = np.array([[1,2,3],[4,5,6]])
print("Original 2D array:\n", arr)
print("Sum along columns (axis=0):", arr.sum(axis=0))
print("Sum along rows (axis=1):", arr.sum(axis=1))
```
