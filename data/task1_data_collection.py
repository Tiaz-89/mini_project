import requests
import time
import random
import json
from datetime import datetime

now = datetime.now()
URL = "https://hacker-news.firebaseio.com/v0/"
URL_ID = "https://hacker-news.firebaseio.com/v0/item/"
headers = {"User-Agent": "TrendPulse/1.0"}

categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm", "network"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global", "korea","england","south","north","west","east","iran"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome", "earth", "moon"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def get_ids():
    try:
      response = requests.get(URL +  "topstories.json", headers=headers)
      if response.status_code == 200:
        return response.json()
    except Exception as e:
      print(e)

def get_story(item_id):
    try:
      response = requests.get(URL_ID + f"{item_id}.json", headers=headers)
      if response.status_code == 200:
        return response.json()
    except Exception as e:
      print(e)

def categorize(title):
    title = title.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title:
               return category
    return "N/A"


ids = get_ids()

result = []

for category in categories.keys():

    for id in ids:
        story = get_story(id)
        
        if not story:
            continue

        detected_category = categorize(story["title"])
        
        result.append({
            "post_id": story["id"],
            "title": story["title"],
            "category": detected_category,
            "score": story["score"],
            "num_comments": story.get("descendants", 0), # some descendants are missing so using this way to get this field
            "author": story["by"],
            "collected_at": now.strftime("%A, %B %d, %Y %H:%M:%S")
        })
        if len(result) >= 250:
            break

    time.sleep(2)

selected_result = random.sample(result, 100) # I have collected 250 records in which, I am just selecting 100 records randomly

# Saving it in json file    
with open('trends.json', 'w') as file:
    json.dump(selected_result, file)

print(f"Collected {len(selected_result)} stories. Saved to data/trends.json")

# Below is extra code to see the count of each category
NA = 0
technology = 0
world_news = 0
science = 0
sports = 0
entertainment = 0

for item in selected_result:
    if item["category"] == "technology":
        technology += 1
    elif item["category"] == "worldnews":
        world_news += 1
    elif item["category"] == "sports":
        sports += 1
    elif item["category"] == "science":
        science += 1
    elif item["category"] == "entertainment":
        entertainment += 1
    else:
        NA += 1

print("Count of 'NA' category:", NA)
print("Count of 'technoloy' category:", technology)
print("Count of 'worldnews' category:", world_news)
print("Count of 'sports' category:", sports)
print("Count of 'science' category:", science)
print("Count of 'entertainment' category:", entertainment)