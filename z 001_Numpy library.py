import numpy as num 

# Numpy Lib. > Creating Array :
np_1 = num.array([5, 4, 3, 2, 1])
np_2 = num.array([[9,7,5], [1,3,7], [8,6,2]])

print(type(np_1), np_1)
print(type(np_2), np_2)

# Zeros, Ones, eye and random.rand :
Zeros = num.zeros((4,4))
Ones = num.ones((3,2))
Identity = num.eye(5,5)
Random_ar = num.random.rand(3,2)
print(Zeros)
print(Ones)
print(Identity)
print(Random_ar)

# Array properties :
print("Size: ", np_1.size)
print("Data Type: ", np_2.dtype)
print("Shape: ", np_1.shape)
print("Dimensions :", np_2.ndim)

# Index and Slicing:
print("Index (found) :", np_2[1,2])  # list in >>> get 1st_list >>> get 2nd value in 1st_list... (0,1,2,... index) 
print("Row :", np_2[0])
print("Sliced array :", np_1[1:4])

xy = num.array([[[14,25,39],[44,55,60],[75,89,98]]])
print(xy[0,2,0])

# Transposed and reshape :
trans = np_2.T                      # Auto Trans
print("Transposed :", trans)

reshape = np_1.reshape(5,1)         # Reshape Method row change to column and column change to row
print("Reshape :", reshape)

# import numpy as num 
np_3 = num.array([[12,23,34,45], [1,2,3,4]])
reshape_I = np_3.reshape(4,2)
print("Reshape_I", reshape_I)

# Mathematical Operations
npy1 = num.array([1, 3, 5, 7, 9])
npy2 = num.array([10, 30, 50, 70, 90])

sum_array = npy1 + npy2
div_array = npy2 / npy1
prod_array = npy1 * npy2
power_array = num.power(npy1, 3)
sqrt_array = num.sqrt(npy2)

print("Sum :", sum_array)
print("Division :", div_array)
print("Product : ", prod_array)
print("Power :", power_array)
print("square Root :", sqrt_array)
