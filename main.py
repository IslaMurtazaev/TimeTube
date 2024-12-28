import json
import csv
from datetime import datetime
from collections import defaultdict

from topic_counter_extractor import extract_topic_list

# Input JSON file path
input_json_path = "watch-history2.json"
# Output directory for CSV files
output_directory = "output/"


def parse_json_to_monthly_csv(json_path, output_dir):
    try:
        # Load JSON data
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # Organize data by month
        monthly_data = defaultdict(list)
        for item in data:
            # Filter out google ads
            if item.get("details", [{"name": ""}])[0].get("name") == "From Google Ads":
                continue
            title = item.get("title", "").removeprefix("Watched ")
            # Filter out removed videos with no title
            if title.startswith("https"):
                continue
            time = item.get("time", "")

            # Parse the time to extract year and month
            try:
                date_obj = datetime.fromisoformat(time.replace("Z", "+00:00"))
                month_key = date_obj.strftime("%Y-%m")
                monthly_data[month_key].append(title)
            except ValueError:
                print(f"Skipping invalid time format: {time}")

        previous_month_topics = []
        # Write each month's data to a separate CSV file
        for month, titles in reversed(monthly_data.items()):
            print('month', month)

            # send a prompt to Open AI API to get a list of topics and their count
            topics = extract_topic_list(titles, previous_month_topics)

            previous_month_topics = topics

        print(f"CSV files created successfully in {output_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the parser
parse_json_to_monthly_csv(input_json_path, output_directory)
