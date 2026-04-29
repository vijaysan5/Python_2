import matplotlib.pyplot as mplt
import numpy as num

# LINE PLOT >>> Waves
x = num.linspace(0, 9, 50)
y = num.sin(x)
mplt.plot(x, y, label="create wave", color='red', linestyle='-', linewidth=1)
mplt.xlabel("X Row")
mplt.ylabel("Y Row")
mplt.title("Line Plot (Wave)")
mplt.legend()
mplt.grid()
mplt.show()


# SCATTER PLOT >>> Dot Marking
x_scatter = num.array([10,34,25,57,45,23,12,38])
y_scatter = [12,43,52,14,34,25,57,24]
mplt.figure(figsize= (6, 6))
mplt.scatter(x_scatter, y_scatter, color="blue", marker= "o", label="Data Point")
mplt.xlabel("X Row")
mplt.xlabel("Y Row")
mplt.title("Data Scatter plot Marker")
mplt.legend()
mplt.grid()
mplt.show()


#  BAR CHART >>> Data Bar
x_Categories = ['8th Std', '9th Std', '10th Std', '11th Std', '12th Std']
y_Values = [79.8, 99.8, 100, 90.5, 100]
mplt.figure(figsize= (8, 5))
mplt.bar(x_Categories, y_Values, color= ['blue', 'yellow', 'purple', 'red', 'green'])
mplt.xlabel("________Classes________")
mplt.ylabel("Exam Percentage")
mplt.title("Bar Chart")
mplt.show()


# HORIZONTAL BAR CHART >>> Data Bar ===>
mplt.figure(figsize= (8, 5))
mplt.barh(x_Categories, y_Values, color= ['blue', 'yellow', 'lightgreen', 'red', 'green'])
mplt.xlabel("Exam Percentage")
mplt.ylabel("Classes")
mplt.title("Horizontal Bar Chart")
mplt.show()


# HISTROGRAM CHART
value = num.random.randn(500)
mplt.figure(figsize= (8, 5))
mplt.hist(value, bins= 25, color= "#8982f1", edgecolor="#5f2121")
mplt.xlabel("Random bar value")
mplt.ylabel("values")
mplt.title("Histrogram Chart")
mplt.show()


# PIE CHART 
Variable = ['Tamil', 'English', 'Maths', 'Hindi', 'Activity'] 
v_val = [19.1, 20.99, 14.10, 15.90, 30]
mplt.figure(figsize= (10, 10))
mplt.pie(v_val, labels=Variable, autopct='%1.1f%%', colors=["#7876df", "#01eebb", "#b54fd4", "#3106f0", "#f70d0d"])
mplt.title("Pie Chart")
mplt.show()


# BOX PLOT
""" Box_value = [[12,54], [68,76], [98,89]]
mplt.figure(figsize= (8, 6))
mplt.boxplot(Box_value, patch_artist=True, labels=['AB', 'CD', 'EF'])
mplt.title("Box Plot")
mplt.show() """
Box_value = [num.random.rand(100), num.random.randn(100), num.random.randn(100)]
mplt.figure(figsize= (8, 6))
mplt.boxplot(Box_value, patch_artist=True, labels=['AB', 'CD', 'EF'])
mplt.title("Box Plot")
mplt.show()


# VIOLIN PLOT
vio_value = [num.random.randn(500), num.random.randn(100), num.random.randn(50), num.random.randn(1000)]
mplt.figure(figsize= (8,6))
mplt.violinplot(vio_value)
mplt.title("Violin plot")
mplt.show()


# STEM PLOT
x_stem = num.linspace(0, 10, 25)
y_stem = num.sin(x_stem)
mplt.figure(figsize= (8,5))
mplt.stem(x_stem, y_stem, linefmt= "b-", markerfmt= "bo", basefmt = "r-")
mplt.title("Stem Plot")
mplt.show()


# SUBPLOTS >>> Multiple Graph
fig, axes_san = mplt.subplots(2, 2, figsize=(10,8))

axes_san[0, 0].plot(x, y, label="create wave", color='red', linestyle='-', linewidth=1)
axes_san[0, 0].set_title("I = Line Plot")

axes_san[0, 1].scatter(x_scatter, y_scatter, color="green", marker= "o", label="Data Point")
axes_san[0, 1].set_title("II = Scatter Plot")

axes_san[1, 0].bar(x_Categories, y_Values, color= ['blue', 'yellow', 'purple', 'red', 'green'])
axes_san[1, 0].set_title("III = Bar Chart")

axes_san[1, 1].stem(x_stem, y_stem, linefmt= "b-", markerfmt="bo", basefmt = "r-")
axes_san[1, 1].set_title("IV = Stem Plot")

mplt.tight_layout()
mplt.show()


# Plot Style Checking
import matplotlib.pyplot as mplt
print(mplt.style.available)

# mplt.style.use('')


"""___SEABORN___"""
# kind = "hist" >>> bar > box type 
# kind = "ecdf" >>> step type
# kind = "kde"  >>> curved type
""" 
import matplotlib.pyplot as mplt
import seaborn as sb
con_box = sb.displot([1, 3, 5, 7, 9])   # ==> Normal hist type  
print("Created 'hist' type seaborn", type(con_box))
mplt.show()

con_line = sb.displot([0,1,2,3,4,5], kind="kde") 
print("Created 'kde' type seaborn", type(con_line))
mplt.show()

con_step = sb.displot([1,3,5,7,9], kind="ecdf")
print("Created 'ecdf' type seaborn", type(con_step))
mplt.show() """
