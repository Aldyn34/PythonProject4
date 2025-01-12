import requests
from bs4 import BeautifulSoup
import csv
import json


class KinoPoiskParser:
    def __init__(self, base_url="https://www.kinopoisk.ru/lists/movies/top/"):
        self.base_url = base_url
        self.movies = []

    def fetch_movies(self, year_from=2010, year_to=2015):


        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, 'html.parser')


        movie_list = soup.find_all('div', class_='desktop-list-main')

        for movie in movie_list:
            title = movie.find('span', class_='movie-title').text.strip()
            rating = movie.find('span', class_='rating').text.strip()
            year = movie.find('span', class_='year').text.strip()

            if year_from <= int(year) <= year_to:
                self.movies.append({
                    "title": title,
                    "rating": rating,
                    "year": year
                })

    def export_to_csv(self, filename="movies.csv"):

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "rating", "year"])
            writer.writeheader()
            writer.writerows(self.movies)

    def export_to_json(self, filename="movies.json"):

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.movies, file, ensure_ascii=False, indent=4)

    def get_movies(self):
       
        return self.movies
