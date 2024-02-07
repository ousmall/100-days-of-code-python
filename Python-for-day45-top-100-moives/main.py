import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)

movie_page = response.text

movie_text = BeautifulSoup(movie_page, "html.parser")

movie_names = movie_text.select(".listicleItem_listicle-item__title__BfenH")

movie_name = [each_name.get_text() for each_name in movie_names]

movie_list = list(reversed(movie_name))

for each_movie in movie_list:
    top_100_list = f"{each_movie}\n"

    try:
        with open("movies.txt", "a") as file:
            file.write(top_100_list)
    except FileNotFoundError:
        with open("movies.txt", "w") as file:
            file.write(top_100_list)
