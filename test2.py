import pandas as pd

capitals = {
    "Countries": ["India", "Germany", "Peru", "Norway", "Russia", "Saudi Arabia", "Indonesia"],
    "Capital": ["New Delhi", "Berlin", "Lima", "Oslo", "Moscow", "Riyadh", "Jakarta"],
    "Population(M)": [1477, 84.5, 34.6, 5.67, 143.5, 35.3, 287]
}

dataFrame = pd.DataFrame(capitals, index=[1, 2, 3, 4, 5, 6, 7])

new_countries = pd.DataFrame([{"Countries": "Maldvies", "Capital": "Male", "Population(M)": 0.53}, 
                              {"Countries": "Denmark", "Capital": "Copenhagen", "Population(M)": 6.02}], index=[8, 9])

dataFrame = pd.concat([dataFrame, new_countries])

print(dataFrame)