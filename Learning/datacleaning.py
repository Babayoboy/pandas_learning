import pandas as pd

data = pd.read_csv("testdataset/data.csv")

# Drop irrelevant column

# data = data.drop(columns=["Flag Age (Years)", "Country Age (Years)"])

#Handle Missing data
# data = data.dropna(subset=["Office Holder Age (Years)"])
# data = data.fillna({"Office Holder Age (Years)": "Dont know"})

#Fix inconsistent values
# data["Continent"] = data["Continent"].replace({"AFRICA":"Africa", "EUROPE": "Europe"})

#Strandarzie text
# data["Capital City"] = data["Capital City"].str.lower()

# Fix data type
# data["Office Holder Age (Years)"] = data["Office Holder Age (Years)"].astype(int)

#Remove duplicate value
data = data.drop_duplicates()

print(data.to_string())