import pandas as pd

data = pd.read_csv("data/data.csv")

worldWar2End = 1945;
# countriesFormedAfter = data[data["Country Formation Year"] >= worldWar2End]
# print(countriesFormedAfter)

senior = 60
# officeHolderAreSeniorCitizen = data[data["Office Holder Age (Years)"] >= 60]
# print(officeHolderAreSeniorCitizen)

# country_FoundationOrFlag_AndOfficeHolderAgeIsSame = data[(data["Office Holder Age (Years)"] == data["Country Age (Years)"]) | (data["Office Holder Age (Years)"] == data["AC Age (Years)"])]
# print(country_FoundationOrFlag_AndOfficeHolderAgeIsSame)

# country_FoundationAndFlag_AndOfficeHolderAgeIsSame = data[(data["Office Holder Age (Years)"] == data["Country Age (Years)"]) & (data["Office Holder Age (Years)"] == data["Flag Age (Years)"])]
# print(country_FoundationAndFlag_AndOfficeHolderAgeIsSame)