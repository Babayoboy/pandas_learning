import pandas as pd

capitals = {"India": "New Delhi", "Kenya": "Nirobi", "Iran": "Tehran", "Iraq": "Damascus", "Timore-leste": "Delhi", "Azerbaijan": "Baku"}

series =  pd.Series(capitals)

series.loc["Timore-leste"] = "Dilli"

print(series.loc["Iraq"])

print(series)