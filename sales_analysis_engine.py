import pandas as pd

df=pd.read_csv("sales_data.csv")

print(df)

df["Profit"] = df["Revenue"] - df["Cost"]
df["Margin"] = (df["Profit"] / df["Revenue"]) * 100

print(df)

print("Total Revenue:", df["Revenue"].sum())
print("Total Profit:", df["Profit"].sum())

print("\n Profit by Region:")
print(df.groupby("Region")["Profit"].sum())

print("\n Top Products by Profit:")
print(df.sort_values(by="Profit",ascending=False))

print("\n Low Margin Products:")
print(df[df["Margin"]<30])

print("\n--- Scenario Simulation: Cost Increase 10% ---")

df["New_Cost"] = df["Cost"] * 1.10
df["New_Profit"] = df["Revenue"] - df["New_Cost"]
df["New_Margin"] = (df["New_Profit"] / df["Revenue"]) * 100

print(df[["Product", "Region", "New_Cost", "New_Profit", "New_Margin"]])

print("\n--- Multi Scenario Simulation ---")

scenarios = [0, 5, 10, 20]

for s in scenarios:
    df[f"Cost_{s}%"] = df["Cost"] * (1 + s/100)
    df[f"Profit_{s}%"] = df["Revenue"] - df[f"Cost_{s}%"]
    df[f"Margin_{s}%"] = (df[f"Profit_{s}%"] / df["Revenue"]) * 100

print(df)

import matplotlib.pyplot as plt

df.plot(x="Product", y=["Margin", "Margin_10%", "Margin_20%"], kind="bar")
plt.title("Margin Sensitivity Analysis")
plt.ylabel("Margin %")

plt.savefig("margin_sensitivity_analysis.png", dpi=300)
plt.show()