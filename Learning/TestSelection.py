import pandas as pd

userRespose = input("Enter the country you want to search for: ")



data = pd.read_csv("data/data.csv", index_col="Country")

try:
    print(data.loc[userRespose])
except KeyError:
    print(f"{userRespose} Not found")