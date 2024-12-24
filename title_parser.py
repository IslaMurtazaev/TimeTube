import json
import csv

# Input JSON file path
input_json_path = "watch-history.json"
# Output CSV file path
output_csv_path = "output.csv"


def parse_json_to_csv(json_path, csv_path):
    try:
        # Load JSON data
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # Open CSV file for writing
        with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write the header row
            csv_writer.writerow(["Title", "Time"])

            # Iterate through JSON items and write to CSV
            for item in data:
                # Filter out google ads
                if item.get("details", [{"name": ""}])[0].get("name") == "From Google Ads":
                    continue
                title = item.get("title", "").removeprefix("Watched ")
                # Filter out removed videos with no title
                if title.startswith("https"):
                    continue
                time = item.get("time", "")
                csv_writer.writerow([title, time])

        print(f"CSV file created successfully at {csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the parser
parse_json_to_csv(input_json_path, output_csv_path)
