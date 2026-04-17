import pandas as pan
import numpy as num

# List Data To Pandas Series  >>> 
Data_san = [15, 25, 55, 75, 85, 95]
san_Series = pan.Series(Data_san)
# print(san_Series)

# Change Index Values >>>
San_ind = pan.Series(Data_san, index= ['One_', 'Two_', 'Three_', 'Four_', 'Five_', 'Six_'])
# print(San_ind)

"_____Data Analyse_____"
""" print("Data type of Series :", San_ind.dtype)
print("Index of Series :", San_ind.index)
print("Value of Series :", San_ind.values)
print("Dimension of Series :", San_ind.ndim)
print("Size of Series :", san_Series.size)
print("Shape of Series :", San_ind.shape)
print("Is Empty Series...? :", San_ind.empty) """

Data = num.array([[498,450,360], [489,443,389], [479,445,385]])
D_Frame = pan.DataFrame(Data, columns=['1st', '2nd','3rd'], index= ['10_A', '10_B', '10_C'])
print(D_Frame)

Data_Dict = {
    'NAME' : ['Abhi', 'Bhuvi', 'Cyndhiya', 'Dhanya'],
    'POSITION' : ['Managing Dept.', 'Developer Dept.', 'Head Dept.', 'Lab Dept.'],
    'INCOME' : [90000, 81000, 88000, 75000],
    'LEVEL' : ['Level 10', 'Level 5', 'Level 8', 'Level 9']
}
Data_f = pan.DataFrame(Data_Dict)
print("\n Data Frame :")
print(Data_f)

Data_f.to_excel('comp_exsheet.xlsx', index=False)
Data_f.to_csv('comp_csv.csv', index=False)
print("Data Saved Successfully...")
read = pan.read_csv('comp_csv.csv')
print("\n CSV _ Reading File : >>>")
print(read)

print("\nInformation :\n", read.info())
print("\nDescribe :\n", read.describe())
print("\nColumns :\n", read.columns)
print("\nData Type :\n", read.dtypes)
print("\nIndex Value :\n", read.index)
print("\nValue of Data_f :\n", read.values)
print("\nDimension of Data_f :", read.ndim)
print("\nSize of Data_f :", read.size)
print("\nShape of Data_f :", read.shape)
print("\nIs Empty ? :", read.empty)

print("\nSelect s Columns :\n", read['NAME'])
print("\nSelect a Row :\n", read.loc[3])
print("\nSelect with Condition :\n", read[read['INCOME'] > 85000])
print("\nSelect index Value :\n", read.iloc[2])

# Add column
read['FESTIVAL BONUS'] = read['INCOME'] * 1.5
print("\nUpdated bonus point :\n", read)

# Drop column
read.drop('FESTIVAL BONUS', axis=1, inplace=True)
print("\nAfter Drop Festival Columns :\n", read)


data = pan.DataFrame({'A' : [12, 23, 45], 'XYZ' :[98, 87, 75]})
print("\nOrginal Data Frame :\n", data)
data_rename = data.rename(columns={'A' : 'ABS'})
print("\nRenamed Data Frame :\n", data_rename)