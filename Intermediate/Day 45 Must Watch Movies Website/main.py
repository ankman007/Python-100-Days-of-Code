from bs4 import BeautifulSoup
import requests
import csv

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
movie_data = response.text
soup = BeautifulSoup(movie_data, 'html.parser')

movies = soup.find_all('h3')
movies_list = [movie.getText().split(')') for movie in movies]

with open(file='100_Must_Watch_Movies.csv', mode='w') as file:
    c_writer = csv.writer(file)
    c_writer.writerows(movies_list)




