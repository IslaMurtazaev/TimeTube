import history_parser
import youtube_client

video_ids_per_year = history_parser.parse_video_ids_by_year("watch-history2.json")

# for year, video_ids in video_ids_per_year.items():
categories = youtube_client.get_video_categories_and_tags(video_ids_per_year['2024'])



