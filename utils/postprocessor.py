def remove_long_tail(topics):
    result = [
        ["Category", "Topic", "Watched times"]
    ]

    for topic in topics:
        try:
            category_name, topic_name, freq = topic.strip().split(',')
            if int(freq) >= 10:
                result.append([category_name, topic_name, freq])
        except ValueError:
            print("topic failed to be parsed", topic)

    return result
