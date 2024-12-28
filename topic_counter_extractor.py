def extract_topic_list(titles, existing_topics):
    print(f"""Convert the watched YouTube video titles into topic names and count the number of videos from the same topic. 
Break them down into more niche topics, a minimum of 10. I need only the topic names and count in this format "topic1: count, topic2: count"

Titles:
{titles}

If you find a same topic in this list (just a reworded version) then use it instead:
{existing_topics}""")
    print()

    return []
