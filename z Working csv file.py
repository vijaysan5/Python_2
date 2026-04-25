import numpy as num
import pandas as pan


csv_reader = pan.read_csv('month_csv.csv')
print("\n CSV _ Reading File : >>>")
print(csv_reader)

print("\nInformation :\n", csv_reader.info())
print("\nDescribe :\n", csv_reader.describe())
print("\nColumns :\n", csv_reader.columns)
print("\nData Type :\n", csv_reader.dtypes)
print("\nIndex Value :\n", csv_reader.index)
print("\nValue of CSV file :\n", csv_reader.values)
print("\nDimension of CSV file :", csv_reader.ndim)
print("\nSize of CSV file :", csv_reader.size)
print("\nShape of CSV file :", csv_reader.shape)
print("\nIs Empty ? :", csv_reader.empty)

















print("\nData Analyse :_________")
""" print("Data type of Series :", csv_reader.dtype)
print("Index of Series :", csv_reader.index)
print("Value of Series :", csv_reader.values)
print("Dimension of Series :", csv_reader.ndim)
print("Size of Series :", csv_reader.size)
print("Shape of Series :", csv_reader.shape)
print("Is Empty Series...? :", csv_reader.empty) """