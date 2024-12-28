import history_parser
import youtube_client
import csv_generator


video_ids_per_year = history_parser.parse_video_ids_by_year("watch-history2.json")

categories = youtube_client.get_video_categories_and_tags(video_ids_per_year['2024'])

category_names = youtube_client.get_category_names(categories.keys())

csv_generator.write('output.csv', categories, category_names)

