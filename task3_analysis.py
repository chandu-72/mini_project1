import pandas as pd
import numpy as np
import os

# Load data
file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)

# 1️⃣ Load and Explore
print(f"Loaded data: {df.shape}")

print("\nFirst 5 rows:")
print(df.head())

print("\nShape:", df.shape)

# Averages
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score : {avg_score:.2f}")
print(f"Average comments: {avg_comments:.2f}")

# 2️⃣ NumPy Analysis
scores = df["score"].values

print("\n--- NumPy Stats ---")
print(f"Mean score : {np.mean(scores):.2f}")
print(f"Median score : {np.median(scores):.2f}")
print(f"Std deviation: {np.std(scores):.2f}")
print(f"Max score : {np.max(scores)}")
print(f"Min score : {np.min(scores)}")

# Category with most stories
top_category = df["category"].value_counts().idxmax()
top_count = df["category"].value_counts().max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")

# Most commented story
max_comments_row = df.loc[df["num_comments"].idxmax()]

print(f"\nMost commented story: \"{max_comments_row['title']}\" - {max_comments_row['num_comments']} comments")

# 3️⃣ Add New Columns

# Engagement
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Popular
df["is_popular"] = df["score"] > avg_score

# 4️⃣ Save result
os.makedirs("data", exist_ok=True)
output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")