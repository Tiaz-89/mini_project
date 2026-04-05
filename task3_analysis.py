# import numpy as np
# import pandas as pd

# # Loading and exploring
# df = pd.read_csv("data/trends_clean.csv")
# print("First 5 rows:")
# print(df.head(5))
# print("--------------------------------------------")
# print("Shape of DataFrame:")
# print(df.shape)
# print("--------------------------------------------")
# print("Average of score and num_comments:")
# print(df[["score","num_comments"]].mean())
# print("--------------------------------------------")

# # Analysis with Numpy 
# score_series = df["score"]
# print(f"mean : {np.mean(score_series)} , median : {np.median(score_series)} , standard deviation : {np.std(score_series)}")
# print(f"Highest score : {np.max(score_series)} , lowest score : {np.min(score_series)}")

# # Analysing with pandas
# category_count = df["category"].groupby(df["category"]).count()
# print(f"category '{category_count.idxmax()}' has the most stories")

# row = df.loc[df["num_comments"].idxmax()]
# print(f"title : {row["title"]} , comment count : {row["num_comments"]}")

# # Adding new columns
# df["engagement"] = df ["num_comments"]/(df["score"]+1)
# df["is_popular"] = df ["score"] > df["score"].mean()

# # Saving to csv file
# df.to_csv("data/trends_analysed.csv", index = False)