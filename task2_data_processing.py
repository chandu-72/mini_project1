import pandas as pd
import os

# File path
file_path = "data/trends.json"

# 1️⃣ Load JSON file
df = pd.read_json(file_path)

print(f"Loaded {len(df)} stories from {file_path}")

# 2️⃣ Clean the Data

# Remove duplicates
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Remove missing values
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Convert data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low quality (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Strip whitespace
df["title"] = df["title"].str.strip()

# 3️⃣ Save as CSV
os.makedirs("data", exist_ok=True)
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)

print(f"Saved {len(df)} rows to {output_file}")

# 4️⃣ Summary: stories per category
print("\nStories per category:")
print(df["category"].value_counts())