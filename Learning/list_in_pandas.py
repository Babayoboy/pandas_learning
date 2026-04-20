import pandas as pd

# Series

data = [100, 102, 104, 106, 108, 200, 202]     #dtype = int64
# data = [100.1, 102.2, 104.3]   #dtype = float64
# data = ["A", "N", "H"]   #dtype = str
# data = [True, False, True]   #dtype = bool

series = pd.Series(data, index=["Room #1", "Room #2", "Room #3", "Room #4", "Room #5", "Room #6", "Room #7"])

series.iloc[0] = 101 #Use iloc for index location

series.loc["Room #3"] = 103 #Use loc for lable location

# print(series.loc["Room #2"])
# print(series.iloc[1])
# print(series[series >= 108]) #prints all the values equal to or greater than 108
# print(series[series < 108]) #prints all the values less than 108
print(series)