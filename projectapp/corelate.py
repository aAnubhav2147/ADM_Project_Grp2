import numpy as np 

import pandas as pd 

def get_corelation(x, y):
  print(x + " " + y)
  data = pd.read_csv("Test/update2q1-15.csv") 
  list1= data.columns.values
  print(list1)
  x = data[x].corr(data[y]) 
  #print(data.corr())
  #print(x)
  return x