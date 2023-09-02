import os
import re
import csv
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")


def movies_from_csv():
    with open('oscar_winners.csv') as csv_file:
        movies = csv.DictReader(csv_file)
        movies_to_csv(movies)


def movies_to_csv(movies):
    headers = ['Movie Title', 'Runtime', 'Genre',
               'Oscar Wins', 'Award Wins',
               'Award Nominations', 'Box Office',
               'Rated', 'Released', 'Director']
    with open('movies.csv', 'w') as movies_csv:
        csv_writer = csv.DictWriter(movies_csv, fieldnames=headers)
        csv_writer.writeheader()
        for movie in movies:
            imdb_id = movie['IMDB']
            movie_from_api(imdb_id, csv_writer)


def clean_award_counts(pattern, text):
    return sum(int(num) for num in re.findall(pattern, text))


def movie_from_api(imdb_id, csv_writer):
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}"
    try:
        response = requests.get(url)
        data = response.json()
        runtime = int(data['Runtime'].split()[0])
        released = datetime.strptime(data['Released'],
                                     '%d %b %Y').date().strftime('%Y-%m-%d')
        awards = data['Awards']
        oscar_wins = clean_award_counts(r'Won (\d+) Oscar', awards)
        award_wins = clean_award_counts(r'(\d+) win', awards)
        nominations = clean_award_counts(r'(\d+) nomination', awards)
        box_office = int(data['BoxOffice'][1:].replace(',', ''))

        csv_writer.writerow({
            'Movie Title': data['Title'],
            'Runtime': runtime,
            'Genre': data['Genre'],
            'Oscar Wins': oscar_wins,
            'Award Wins': award_wins,
            'Award Nominations': nominations,
            'Box Office': box_office,
            'Rated': data['Rated'],
            'Released': released,
            'Director': data['Director']
        })
    except Exception as e:
        print(e)


if __name__ == "__main__":
    movies_from_csv()
