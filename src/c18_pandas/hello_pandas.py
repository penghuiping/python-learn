# coding=utf-8
import numpy as np
import pandas as pd

df = pd.read_excel("/Users/penghuiping/Programming/repository/python-learn/src/c18_pandas/test.xlsx", sheet_name="Sheet1")
print(df.to_dict)