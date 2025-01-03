# TimeTube

### Description
Extracts a list of interests based on your YouTube history.

It takes your YouTube history of watched videos as input and returns a CSV file with weighted interests 
that can be used for visualizations or further analysis.

![interest_visuzalization.gif](readme_media%2Finterest_visuzalization.gif)

Note: visualization was not part of the project, I used [Flourish Studio](https://app.flourish.studio/) to 
generate a free preview. 

### Prerequisites
You need to download your history and get two API keys. One is YouTube API key to get some extra metadata and 
the other is OpenAI API key to help with categorization.

### Setup
1. Start by cloning the repository and entering the project directory
2. Install python 3 if you don't have it already
3. Setup python virtual environment `python -m venv venv`
4. Activate the virtual environment `source ./venv/bin/activate`
5. Install python packages `pip install -r requirements.txt`
6. Download your YouTube History from Google Takeout and select JSON format.
![youtube_history1.png](readme_media%2Fyoutube_history1.png)
 Deselect all other services.
![youtube_history2.png](readme_media%2Fyoutube_history2.png)
7. Unpack the downloaded content, find `watch-history.json` in `YouTube and YouTube Music/history/`
and move it to the project root directory
8. Generate YouTube and OpenAI API keys and pase them in `.env` file in the root of the project
```
YOUTUBE_API_KEY=***
OPENAI_API_KEY=***
```
9. Run the program `python .`
