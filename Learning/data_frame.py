import pandas as pd

data = {"Surname": ["Modi", "Gandhi", "Stalin", "Sharma"],
        "Age": [75, 55, 73, 57]}


df = pd.DataFrame(data, index=["Politician 1", "Politician 2", "Politician 3", "Politician 4"])

df["Position"] = ["PM India", "LoP India", "CM Tamil Nadu", "CM Assam"]

new_rows = pd.DataFrame([{"Surname": "Adityanath", "Age": 53, "Position": "CM Uttar Pradesh"}, 
                         {"Surname": "Dhami", "Age": 50, "Position": "CM Uttrakhand"}], 
                         index=["Politician 5", "Politician 6"])
df = pd.concat([df, new_rows])

# print(df.loc["Politician 3"])
# print(df.iloc[1])
print(df) 