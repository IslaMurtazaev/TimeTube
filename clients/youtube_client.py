import collections
import requests
import os
from dotenv import load_dotenv

load_dotenv()


YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def get_categories(video_ids_per_year):
    print("Request Youtube metadata for watched videos")
    categories = get_video_categories_and_tags(video_ids_per_year['2024'])
    category_names = get_category_names(categories.keys())

    # replace category_id with category_name
    for category_id in list(categories.keys()):
        category_name = category_names[category_id]
        categories[category_name] = categories.pop(category_id)

    print(f"\nYoutube Categories: {categories}\n")
    return categories


def get_category_names(category_ids):
    category_ids_param = ",".join(category_ids)
    url = f"{YOUTUBE_API_URL}/videoCategories?id={category_ids_param}&key={YOUTUBE_API_KEY}&part=snippet"

    data = requests.get(url).json()

    result = dict()
    for item in data.get('items', []):
        category_name = item['snippet']['title']
        category_id = item['id']

        result[category_id] = category_name

    return result


def get_video_categories_and_tags(video_ids):
    result = dict()

    for i in range(0, len(video_ids), 50):
        video_ids_batch = video_ids[i:i+50]
        video_ids_param = ",".join(video_ids_batch)

        url = f"{YOUTUBE_API_URL}/videos?id={video_ids_param}&key={YOUTUBE_API_KEY}&part=snippet"

        data = requests.get(url).json()

        items = data.get('items', [])
        for item in items:
            details = item['snippet']
            category_id = details['categoryId']
            tags = details.get('tags', [])

            if category_id not in result:
                result[category_id] = collections.Counter()

            for tag in tags:
                result[category_id][tag] += 1

    return result
