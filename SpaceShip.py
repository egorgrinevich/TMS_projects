
import pandas as pd
df = pd.read_csv("train.csv", sep=',')

print(df.head(10))

#print(df.tail(10))

#print(df.columns)

print(df.info())
print(df["Age"].agg(["mean", "max", "min"]))

print(df[["Age", "VIP"]][df["Age"] >= 1].groupby("VIP").agg(["mean", "min", "max"]))

print(df[["VIP", "Destination"]].groupby("VIP").agg(["count"]))
print(df[["Age", "Destination"]].groupby("Destination").agg(["count"]))
print(df[["Age", "VIP", "Destination"]].groupby("Destination").agg(["count"]))
print(df[[ "VIP", "RoomService", "Destination", "ShoppingMall"]].groupby("VIP").agg(["count"]))

#df.Destination = df.Destination.apply(lambda x: 1 if x == "55 Cancri e")
print(df[[ "VIP", "RoomService", "Destination", "ShoppingMall"]].groupby("VIP").agg(["count"]))

print(df.describe())