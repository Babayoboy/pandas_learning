import pandas as pd

df = pd.read_csv("data/data.csv", index_col="Country")

#Selection by Column
# print(df["Country"].to_string())
# print(df["Capital City"].to_string())
# print(df["Flag Adoption Year"].to_string())
# print(df["Flag Age (Years)"].to_string())
# print(df["Highest Office Holder"].to_string())
# print(df["Office Holder Age (Years)"].to_string())

# print(df[["Country", "Capital City", "Highest Office Holder"]].to_string())

#Selection by Row
print(df.iloc[109:120:2, 0:4])
# print(df.loc["India":"Tuvalu", ["Capital City", "Flag Age (Years)", "Country Age (Years)"]])