import json
from collections import defaultdict
from datetime import datetime


def parse_video_ids_by_year(json_path):
    try:
        # Load JSON data
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # Organize data by month
        watched_per_year = defaultdict(list)
        for item in data:
            # Filter out google ads
            if item.get("details", [{"name": ""}])[0].get("name") == "From Google Ads":
                continue
            title = item.get("title", "")
            title_url = item.get("titleUrl", "").split('\u003d')[1]
            # Filter out removed videos with no title
            if not title_url or title_url in title:
                continue
            time = item.get("time", "")

            # Parse the time to extract year and month
            try:
                date_obj = datetime.fromisoformat(time.replace("Z", "+00:00"))
                year_key = date_obj.strftime("%Y")
                watched_per_year[year_key].append(title_url)
            except ValueError:
                print(f"Skipping invalid time format: {time}")

        print(f"History parsed successfully")

        return watched_per_year
    except Exception as e:
        print(f"An error occurred: {e}")
