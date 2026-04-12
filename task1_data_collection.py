import requests
import time
import json
import os

# API URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/47712771.json"

headers = {"User-Agent": "TrendPulse/1.0"}

# Categories with keywords
categories = {
    "technology": ["ai", "software", "tech", "computer", "data", "api"],
    "worldnews": ["war", "government", "country", "president"],
    "sports": ["nfl", "nba", "fifa", "sport", "game"],
    "science": ["research", "study", "space", "physics"],
    "entertainment": ["movie", "film", "music", "netflix"]
}

def get_category(title):
    title = title.lower()
    for category, keywords in categories.items():
        for word in keywords:
            if word in title:
                return category
    return "other"

try:
    response = requests.get(TOP_STORIES_URL, headers=headers)
    story_ids = response.json()[:100
                                ]
except:
    print("Error fetching top stories")
    story_ids = []

stories = []

for sid in story_ids:
    try:
        res = requests.get(ITEM_URL.format(sid), headers=headers)
        data = res.json()

        if data and "title" in data:
            story = {
                "post_id": data.get("id"),
                "title": data.get("title"),
                "category": get_category(data.get("title", "")),
                "score": data.get("score", 0),
                "num_comments": data.get("descendants", 0)
            }
            stories.append(story)

    except:
        print(f"Error fetching story {sid}")

    time.sleep(0.1)

# Create folder
os.makedirs("data", exist_ok=True)

# Save JSON
filename = "data/trends.json"
with open(filename, "w") as f:
    json.dump(stories, f, indent=2)

print(f"Collected {len(stories)} stories. Saved to data/trends.json")