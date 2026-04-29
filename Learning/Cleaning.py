import pandas as pd

data = pd.read_csv("testdataset/data.csv")

data["CAPITAL city"].replace({"NaN": "N/A"})

print(data)