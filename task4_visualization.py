import pandas as pd
import matplotlib.pyplot as plt
import os

# ======================
# 1 Setup
# ======================
df = pd.read_csv("data/trends_analysed.csv")

os.makedirs("outputs", exist_ok=True)

# ======================
# 2 Chart 1: Top 10 Stories by Score
# ======================
top10 = df.sort_values(by="score", ascending=False).head(10)

# shorten titles
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure()
plt.barh(top10["short_title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()

plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# ======================
# 3 Chart 2: Stories per Category
# ======================
category_counts = df["category"].value_counts()

plt.figure()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")
plt.close()

# ======================
# 4 Chart 3: Score vs Comments
# ======================
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure()
plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.close()

# ======================
# Bonus: Dashboard
# ======================
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Chart 1
axes[0].barh(top10["short_title"], top10["score"])
axes[0].set_title("Top Stories")
axes[0].invert_yaxis()

# Chart 2
axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Categories")

# Chart 3
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")

plt.suptitle("TrendPulse Dashboard")
plt.tight_layout()

plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in outputs/")