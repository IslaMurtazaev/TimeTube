from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def format_category_for_prompt(category_name, tags):
    all_tags = ["Category,Tag,Watched times"]

    for tag, freq in tags.items():
        all_tags.append(f"{category_name},{tag},{freq}")

    return "\n".join(all_tags)


def combine_similar_tags_into_single_topic(categories):
    client = OpenAI(api_key=OPENAI_API_KEY)

    all_topics = []
    for category_name, tags in categories.items():
        print(f"\nStart Processing Category {category_name}\n")

        category_prompt = PROMPT + format_category_for_prompt(category_name, tags)

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": category_prompt
                }
            ]
        )

        print(f"\nFinish Processing Category {category_name}\n")

        category_topics = completion.choices[0].message.content.split("\n")
        print(f"\n Category topics: {category_topics}\n")
        # skip header
        all_topics += category_topics[1:]

    print(f"\n\nAll topics: {all_topics}\n\n")
    return all_topics


PROMPT = """You will be given a table with 3 columns: Category, Tag, Watched times.
A new row starts on a new line and cells are divided using comma delimiter following CSV format.

Don't change the first column "Category", only combine similar tags into a single row and sum the Watched times of all combined rows in a new row.
Return only a resulting table without any other messages, so that I can split the output by lines and get each row.

The task is to combine some of the tags into a common topic for example:
Input:
Category,Tag,Watched times
Science & Technology,clear iPhone storage,1
Science & Technology,clean up iPhone storage space,1
Science & Technology,free up iPhone storage,1
Science & Technology,increase storage iphone,1
Science & Technology,how to get more storage on iphone without paying,1
Science & Technology,how to add more storage to iphone,1
Science & Technology,add storage to iphone,1
Science & Technology,how to clear storage on iphone,1
Science & Technology,how to free storage on iphone,1
Science & Technology,iPhone storage is full,1
Science & Technology,how to reduce storage on iphone,1
Howto & Style,Рецепты в гостях у Вани,1
Howto & Style,блюда из фарша,1
Howto & Style,что приготовить из фарша,1
Howto & Style,из фарша,1
Howto & Style,что приготовить на ужин,1
Howto & Style,рецепты из фарша,1
Howto & Style,блюдо из фарша,1
Howto & Style,макароны с мясом,1
Howto & Style,макароны на сковороде,1
Howto & Style,блюда из макарон,1
Howto & Style,ужин на сковороде,1
Howto & Style,макароны с фаршем,1
Howto & Style,макароны с сыром,1
Howto & Style,на сковороде,1
Howto & Style,макароны,1
Howto & Style,рецепт из фарша,1
Howto & Style,вкуснота из фарша,1
Howto & Style,из фарша блюда,1
Howto & Style,ужин на скорую руку,1
Howto & Style,из фарша на сковороде,1
Howto & Style,рецепты на сковороде,1
Howto & Style,овощи с фаршем на сковороде,1
Howto & Style,ужин из фарша,1
Howto & Style,как приготовить макароны,1
Education,mst,1
Education,prims algorithm,1
Education,prims,1
Education,lazy implementation,1
Education,spanning tree,1
Education,graph theory,1
Education,network,1
Education,Data Structures,1
Education,Graph,1
Education,SpanningTree,1
Education,Prim's Algorithm,1
Education,Graph Theory,1
Education,Prim's,1
Education,Graph Algorithms,1
Education,Prims,1
Education,Prim,1
Education,Prim's Example,1


Should output:
Science & Technology,Free up iPhone storage,11
Howto & Style,Food Recipes and Snacks,24
Education,Graph algorithms,17


Here is the actual input needed to be worked on:
"""
