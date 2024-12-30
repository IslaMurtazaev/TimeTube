from utils import csv_generator, history_parser, postprocessor
from clients import open_ai_client, youtube_client

video_ids_per_year = history_parser.parse_video_ids_by_year("watch-history.json")

categories = youtube_client.get_categories(video_ids_per_year)

topics = open_ai_client.combine_similar_tags_into_single_topic(categories)

processed_topics = postprocessor.remove_long_tail(topics)

csv_generator.write('output.csv', processed_topics)
