import requests
# from secrets import genius_client_access_token
from bs4 import BeautifulSoup

# why can't I import variables from other files? just hardcode for now
genius_client_access_token = "jBmnPj48M0-CfNT4Jr1kb1iMYiqRdxHVNJPmTPisIAN9gpKRIYPlB_BTN50GCOZJ"

# 1. use search request to get song info (including id)
def get_song_info(artist, song_name):
    artist_name = artist.lower()
    song_title = song_name.lower()
    headers={"Authorization": "Bearer {}".format(genius_client_access_token)}
    search_url = "https://api.genius.com/search?q="
    q = "{} {}".format(artist_name, song_title)
    q.replace(" ", "%20")
    endpoint = search_url + q
    response = requests.get(endpoint, headers=headers)
    response_json = response.json()

    # error check
    if response_json["meta"]["status"] != 200:
        return False

    for hit in response_json["response"]["hits"]:
        # print(hit["result"]["primary_artist"]["name"])
        # print(hit["result"]["title"])
        if hit["result"]["primary_artist"]["name"].lower() == artist_name and hit["result"]["title"].lower() == song_title:
                # print("success")
                return hit["result"]
        else: 
            return False # either mistyped for Genius doesn't have this song
    
# 2. pass url from get_song_info() to get song lyrics w/ Beautiful Soup
def get_song_lyrics(url):
    headers={"Authorization": "Bearer {}".format(genius_client_access_token)}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    lyrics = soup.find("div", attrs={"class": "lyrics"})
    return lyrics


result = get_song_info("The Weeknd", "high for this")
lyrics = get_song_lyrics(result["url"])
print(lyrics)

    













    # GET SONG REQUEST
    # endpoint = "api.genius.com/songs/{}?text_format=html".format(song_id)
    # headers={"Authorization": "Bearer {}".format(secrets.genius_client_access_token)}
    # response = requests.get(endpoint, headers=headers)
    # response_json = response.json()