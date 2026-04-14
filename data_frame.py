import pandas as pd

data = {"Name": ["Modi", "Gandhi", "Stalin", "Sharma"],
        "Age": [75, 55, 73, 57]}


df = pd.DataFrame(data, index=["Politician 1", "Politician 2", "Politician 3", "Politician 4"])

# print(df.loc["Politician 3"])
# print(df.iloc[1])
print(df)