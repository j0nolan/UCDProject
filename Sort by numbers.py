import numpy as np
import pandas as pd

dataset = pd.read_csv("Batchelor_degrees2017_18.csv")

##look at dataset shape
print(dataset.shape)
##show dataset columns
print(dataset.columns)
##show data types
print(dataset.dtypes)
##sort by Total number of degrees
print(dataset.Total.sort_values)

