import numpy as num 
from scipy import stats

array_One = num.array([1, 3, 5, 7, 9, 3, 1])
array_Three = num.array([10, 30,50, 70, 90, 30, 10])

# Statistical Functions
mean_value = num.mean(array_Three)
median_value = num.median(array_Three)
standard_value = num.std(array_Three)
vars_value = num.var(array_Three)
max_value = num.max(array_Three)
min_value = num.min(array_Three)
mode_value = stats.mode(array_Three)

# Concatenation & Stacking
concatenat = num.concatenate((array_One, array_Three))
stack = num.vstack((array_One, array_Three))

"Printings"
print("Mean Value (numoy): ", mean_value)
print("Median Value (numoy):", median_value)
print("Standard Value :", standard_value)
print("variance :", vars_value)
print("Maximum Value :", max_value)
print("Min Value :", min_value)
print("Mode Value (stats) :", mode_value)
print("Concatenation :", concatenat)
print("Stacking :", stack)

