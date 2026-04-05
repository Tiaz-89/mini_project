# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns


# df = pd.read_csv("data/trends_analysed.csv")

# # Chart 1
# chart_1 = df.sort_values(by="score", ascending=False).head(10)

# plt.barh(chart_1["title"], chart_1["score"])
# plt.title("Top 10 Stories by Score")
# plt.xlabel("Score")
# plt.ylabel("Title")

# plt.savefig("output/chart1_top_stories.png")
# plt.show()


# # Chart 2
# chart_2 = df["category"].groupby(df["category"]).count()
# colors = ["red", "blue", "green", "orange", "purple", "cyan"]

# plt.bar(chart_2.index, chart_2.values, color = colors)
# plt.title("Stories per category")
# plt.xlabel("Category")
# plt.ylabel("Stories count")

# plt.savefig("output/chart2_top_stories.png")
# plt.show()

# # Chart 3
# sns.scatterplot(x="score", y="num_comments", hue="is_popular", data = df) # legend appears automatically
# plt.title("Scores vs Comments")
# plt.xlabel("Scores")
# plt.ylabel("Comments")

# plt.savefig("output/chart3_scatter.png")
# plt.show()

# # Dashboard
# fig, axes = plt.subplots(1, 3, figsize=(18, 5))
# fig.suptitle("TrendPulse Dashboard")

# # -----------------------------------------------------
# # Chart 1

# axes[0].barh(chart_1["title"], chart_1["score"])
# axes[0].set_title("Top 10 Stories by Score")
# axes[0].set_xlabel("Score")
# axes[0].set_ylabel("Title")

# # -----------------------------------------------------
# # Chart 2

# colors = ["red", "blue", "green", "orange", "purple", "cyan"]

# axes[1].bar(chart_2.index, chart_2.values, color=colors)
# axes[1].set_title("Stories per Category")
# axes[1].set_xlabel("Category")
# axes[1].set_ylabel("Stories Count")

# # -----------------------------------------------------
# # Chart 3
# sns.scatterplot(x="score",y="num_comments",hue="is_popular",data=df,ax=axes[2])

# axes[2].set_title("Scores vs Comments")
# axes[2].set_xlabel("Scores")
# axes[2].set_ylabel("Comments")


# plt.tight_layout()
# plt.savefig("output/dashboard.png")
# plt.show()