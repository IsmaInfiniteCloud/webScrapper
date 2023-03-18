import requests
from bs4 import BeautifulSoup
import os

def get_albums(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    album_list = []
    for header in soup.find_all('h2', class_='c-gallery-vertical-slide__title'):
        album_list.append(header.text.strip())

    return album_list

def save_to_file(album_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for album in album_list:
            file.write(album + '\n')

if __name__ == '__main__':
    url = 'https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/james-brown-star-time-2-1063179/'
    file_path = os.path.join('C:', os.sep, 'Users', 'User', 'Desktop', '4 eme Session', '420-A15-BB DÉVELOPPEMENT D\'APPLICATIONS ORIENTÉES', 'Tp de Session', 'album_list.txt')

    album_list = get_albums(url)
    save_to_file(album_list, file_path)
    print("Album list saved to:", file_path)
