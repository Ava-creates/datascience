import numpy as np
import seaborn as sn 
import pandas as pd

data= pd.read_csv("income.csv", )

print(data.info())

#print(data.isnull().sum())

print(data.describe(include="O"))

print(data.corr())