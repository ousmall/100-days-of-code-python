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


# movie_list = []
#
# for each_name in movie_names:
#     movie_name = each_name.get_text()
#     movie_list.append(movie_name)
#
# for index, name in enumerate(reversed(movie_list), 1):
#     # "enumerate" to get index, "reversed" to upside down
#     if name.endswith(", The"):
#         name = "The " + name.split(", ")[0]
#     movie_name = name
#     top_100_list = f"{index}) {movie_name}\n"
#
#     try:
#         with open("movies.txt", "a") as file:
#             file.write(top_100_list)
#     except FileNotFoundError:
#         with open("movies.txt", "w") as file:
#             file.write(top_100_list)
