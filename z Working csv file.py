import numpy as num
import pandas as pan


""" csv_reader = pan.read_csv('month_csv.csv')
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
print("\nIs Empty ? :", csv_reader.empty) """


import pandas as pan
import matplotlib.pyplot as mplt
# csv file to pandas lib >> and matplotlib.pyplot:
wdread = pan.read_csv("weekday.csv")
print("\nReady to Read weekday.csv file :\n", wdread)
wd = wdread
# print(wd)

x_Categories = wd['Name']
y_Values = wd['Numeric']
mplt.figure(figsize= (8, 5))
mplt.barh(x_Categories, y_Values, color= ['green', 'yellow', 'purple', 'pink', 'blue',  'red', 'skyblue'])
mplt.xlabel("Numeric")
mplt.ylabel("Week Day")
mplt.title("Bar Chart")
mplt.show()

sample_read = pan.read_csv("sample.csv")
print("\nReady to Read Sample.csv file :\n",sample_read)
rds = sample_read
x_line = rds['INCOME']
y_line = rds['NAME']
mplt.plot(x_line, y_line, label="Wave", color="#6200ff", linestyle='-', linewidth=2)
mplt.xlabel("Income")
mplt.ylabel("Name")
mplt.title("SALARY DATA >>> lineplot")
mplt.legend()
mplt.grid()
mplt.show()

name = rds['NAME']
value = rds['INCOME']
mplt.figure(figsize=(5, 5))
mplt.pie(value, labels=name, autopct="%1.1f%%", colors=["#7876df", "#01eebb", "#b54fd4", 'skyblue', "pink"])
mplt.title("SALARY DATA >>> pie chart")
mplt.show()

cust = pan.read_csv("customers-100.csv")
print("\nReady to Read weekday.csv file :\n", cust)
stm = cust
x_stem = stm['Subscription Date']
y_stem = stm['First Name']
mplt.figure(figsize=(10, 20))
mplt.stem(x_stem, y_stem, linefmt= "b-", markerfmt= "bo", basefmt = "r-")
mplt.title("Code >>> Stem Plot")
mplt.show()
