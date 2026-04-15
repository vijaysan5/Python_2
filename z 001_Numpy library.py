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

"numpy at."
# Linear Algebra
matrix_mx = num.array([[1,3], [5, 9]])
matrix_nx = num.array([[9, 7], [3, 5]])
matrix_product = num.dot(matrix_mx, matrix_nx)
print("Matrix Product :", matrix_product)

inverse_mx = num.linalg.inv(matrix_mx)
determinant_mx = num.linalg.det(matrix_mx)
print("Inverse :", inverse_mx)
print("Determinant :", determinant_mx)

# Use Random >> in numpy lib
random_float = num.random.rand()
print("Random Value :", random_float)

random_int = num.random.randint(1,50, (3,3))
print("Random Integer Value :", random_int)

random_normal = num.random.normal(0,1,(3,4))
print("Random Normal Distribution :", random_normal)


"Empty Value..."
empty_array = num.empty((3,2))      # get values in storage in comp.
print("Empty :", empty_array)

"Arange Value... (_Arange > linspace > full_)"
Array_one = num.arange(14)
print("Arange Values in 0 ---> 14 :", Array_one)
Array_two = num.arange(0,24, (3))
print("Arange Values in 0 ---> 24 :", Array_two)
Array_linspace = num.linspace(0,10, num=5)
print("Arange linspace Value :", Array_linspace)
Array_full = num.full((3,3), 235)
print("full rows and columns (235) :", Array_full)

"List Value to Array Value Changing Methods..."
List_val = [12, 75, 85, 65, 23, 95]
List_to_Array = num.asarray(List_val)
print("List >> Array :", List_to_Array)
print(type(List_to_Array))
List_val_1 = [54, 69, 38, 97, 15]
List_to_Array_1 = num.array(List_val_1)
print("List >> Array :", List_to_Array_1)

Orginal_arr = num.array([12, 23, 35, 57, 78, 89])
text_x = Orginal_arr.view()
text_c = Orginal_arr.copy()

print("Array Orginal :", Orginal_arr)
print("view Orginal :", text_x)

Orginal_arr[2] = 55
print("Array after change :", Orginal_arr)
print("View after change :", text_x)
print("Copy :", text_c)


"Array >>>>>>  Flatten and Transpose..."
Org_Array = num.array([[1,2,3],
                       [3,4,5]])
Flatten_Array = Org_Array.flatten()
print("Orginal Array :", Org_Array)
print("\nFlatten Array :", Flatten_Array)
print("\nTranspose Array :", Org_Array.transpose())

"Index Value Position >>> use 'where'..."
Org_Arr = num.array([1,3,2,3,4,5,6,7,8,5,9])
Index_where = num.where(Org_Arr == 5)
print("Index Number~5 Value :", Index_where)
print("Index Number~3 Value:", num.where(Org_Arr == 3))

"Sort Value..."
Org_Arr_1 = num.array([9,5,7,1,3])
print("Sort Values :", num.sort(Org_Arr_1))

"Show True Value Only..."
Array_Value = num.array([1,2,3,4,5,6,7,8,9,23])
x = [True, False, True, False, True, False, False, True, False, True]
Show_True = Array_Value[x]
print("True Values :", Show_True)