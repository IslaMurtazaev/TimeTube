import csv


def write(filename, categories, category_names):
    data = [
        ["Category", "Tag", "Watched times"]
    ]
    for category_id, tags in categories.items():
        category_name = category_names[category_id]

        for tag, freq in tags.items():
            data.append([category_name, tag, freq])

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
