import collections
import requests

YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
YOUTUBE_API_KEY = ""


def get_category_name(category_id):
    url = f"{YOUTUBE_API_URL}/videoCategories?id={category_id}&key={YOUTUBE_API_KEY}&part=snippet"

    data = requests.get(url).json()

    return data.get('items')[0]['snippet']['title']


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

    print('result', result)
    return result
