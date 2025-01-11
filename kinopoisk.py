import requests
from bs4 import BeautifulSoup
import json
import csv


class LowRatedMoviesParser:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_movies_data(self):
        response = requests.get(self.base_url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from {self.base_url}")
        return response.text

    def parse_movies_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        movies = []

        # Измените 'div' и 'class_' на актуальные, если структура HTML изменилась
        for movie in soup.find_all('div', class_='search_results'):
            title_tag = movie.find('a', class_='title')
            rating_tag = movie.find('span', class_='rating')
            year_tag = movie.find('span', class_='year')

            if title_tag and rating_tag and year_tag:
                title = title_tag.text.strip()
                rating = float(rating_tag.text.strip().replace(',', '.'))
                year = int(year_tag.text.strip())
                movies.append({
                    'title': title,
                    'rating': rating,
                    'year': year
                })

        # Сортировка фильмов по рейтингу (по возрастанию)
        movies.sort(key=lambda x: x['rating'])

        # Дебаг: вывод количества найденных фильмов
        print(f"Found {len(movies)} movies.")

        return movies

    def save_to_json(self, data, filename='low_rated_movies.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def save_to_csv(self, data, filename='low_rated_movies.csv'):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    def run(self):
        html = self.fetch_movies_data()
        movies = self.parse_movies_data(html)

        if not movies:
            print("No low-rated movies found.")
            return  # Выход, если фильмы не найдены

        self.save_to_json(movies)
        self.save_to_csv(movies)
        print(f"Parsed {len(movies)} low-rated movies.")


if __name__ == "__main__":
    base_url = "https://www.kinopoisk.ru/user/1928945/"
    parser = LowRatedMoviesParser(base_url)
    parser.run()