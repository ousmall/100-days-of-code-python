import requests
from bs4 import BeautifulSoup
import private
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# details: https://spotipy.readthedocs.io/en/2.22.1/


# Todo 1:data from billboard
date = input("Which year do you want to travel back? "
             "\n(Type the date in this format 'YY-MM-DD'): ")

billboard_url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url=billboard_url)

music_page = response.text
music_text = BeautifulSoup(music_page, "html.parser")
# music_names = music_text.select("li ul li h3")


table = music_text.find("div", class_="chart-results-list")  # find the big box
song_titles = table.find_all("h3", class_="a-no-trucate")  # and then find the gadget
artists = table.find_all("span", class_="a-no-trucate")  # add one more element to make precision
song_list = [song.getText().strip() for song in song_titles]
artist_list = [artist.getText().strip() for artist in artists]
# print(song_list)
# print(artist_list)


# Todo 2: tackle the requirement with spotify
# Creates a SpotifyOAuth object, it needs some parameters, for details:
# https://spotipy.readthedocs.io/en/2.13.0/#spotipy.oauth2.SpotifyOAuth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=private.REDIRECT_URI,
        client_id=private.CLIENT_ID,
        client_secret=private.CLIENT_SECRETE_KEY,
        show_dialog=True,
        cache_path="token.txt",
        username="small",
    )
)
user_id = sp.current_user()["id"]


# Todo 3: Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song, artist in zip(song_list, artist_list):
    result = sp.search(q=f"track:{song} year:{year} artist:{artist}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# Todo 4: Creating a private playlist and Adding songs
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# my list:
# https://open.spotify.com/playlist/6wMZ0GHe7TlWYAA94wTexC
