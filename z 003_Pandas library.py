import pandas as pan
import numpy as num

# List Data To Pandas Series  >>> 
Data_san = [15, 25, 55, 75, 85, 95]
san_Series = pan.Series(Data_san)
print(san_Series)

# Change Index Values >>>
San_ind = pan.Series(Data_san, index= ['One_', 'Two_', 'Three_', 'Four_', 'Five_', 'Six_'])
print(San_ind)  

"_____Data Analyse_____"
print("Data type of Series :", San_ind.dtype)
print("Index of Series :", San_ind.index)
print("Value of Series :", San_ind.values)
print("Dimension of Series :", San_ind.ndim)
print("Size of Series :", san_Series.size)
print("Shape of Series :", San_ind.shape)
print("Is Empty Series...? :", San_ind.empty)

Data = num.array([[498,450,360], [489,443,389], [479,445,385]])
D_Frame = pan.DataFrame(Data, columns=['1st', '2nd','3rd'], index= ['10_A', '10_B', '10_C'])
print(D_Frame)