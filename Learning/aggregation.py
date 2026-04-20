import pandas as pd

data = pd.read_json("data/data.json")

# Whole dataframe
# print((data.mean(numeric_only=True)).round(0))
# print((data.median(numeric_only=True)).round(0))
# print(data.sum(numeric_only=True))
# print(data.min(numeric_only=True))
# print(data.max(numeric_only=True))
# print(data.count())

# Single Column
# print(data["Office Holder Age (Years)"].mean().__round__(0))
# print((data["Country Age (Years)"].median()).__round__(0))
# print(data["Country Formation Year"].sum())
# print(data["Flag Age (Years)"].min())
# print(data["Flag Age (Years)"].max())
# print(data["Country"].count())

#groupby
group = data.groupby("Continent")

# print(group["Office Holder Age (Years)"].mean().round(0))
# print(group["Country Age (Years)"].median().round(0))
# print(group["Country Age (Years)"].median().round(0))
# print(group["Country Formation Year"].min())
# print(group["Flag Adoption Year"].max())
# print(group["Country"].count())

