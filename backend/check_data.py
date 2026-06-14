import pandas as pd

df = pd.read_csv("../data/novabite_sales_data.csv")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nShape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())