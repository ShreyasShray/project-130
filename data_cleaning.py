import csv
import pandas as pd

df = pd.read_csv("stars_data.csv")

# Cleaning the data

# print(df.shape)

df = df[df["mass"].notna()]
df = df[df["radius"].notna()]

print(df.shape)

star_data = df.values.tolist()
for data in star_data:
    data.pop(0)

star_data.pop(0)

df = pd.DataFrame(star_data, columns = ["name", "distance", "mass", "radius"])
df.to_csv("final.csv")