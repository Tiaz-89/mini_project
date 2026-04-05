import pandas as pd
import json

# loading the json file
with open("data/trends.json", "r") as file:
  df = pd.DataFrame(json.load(file))

print(f"Loaded {len(df)} stories from data/trends.json\n")
print ("----------------------------------------")
print("Data type:")
print(df.dtypes) # Shows the data type of each columns and confirms score and num_comments are int
print ("----------------------------------------")
print("Missing values:")
print(df.isnull().sum()) # Shows how many missing values are there
print ("----------------------------------------")

# Cleaning the data
df.drop_duplicates(subset="post_id") # Removing the duplicate rows based on post_id field
print(f"After removing duplicates: {len(df)}")
df.dropna(subset=["post_id","title","score"])
print(f"After removing nulls: {len(df)}")
df=df[df["score"] > 5] # Removed the rows where the score is less than 5
print(f"After removing low scores: {len(df)}")
df["category"] = df["category"].fillna("others") # Filling the values none to others
df["title"] = df["title"].str.strip() # removing the white spaces
print ("----------------------------------------\n")

#Saving as csv
df.to_csv("data/trends_clean.csv",index=False)

print(f"Saved {len(df)} rows to data/trends_clean.csv\n")

print("Stories per category:")
print(df["category"].groupby(df["category"]).count())