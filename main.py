import os

import requests
from pathlib import Path
from random import randint
from dotenv import load_dotenv


def check_status(response):
    response.raise_for_status()
    if response.json().get('error'):
        raise requests.exceptions.HTTPError(response=response)


def get_random_comics_number():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    current_comic_number = response.json()['num']
    return randint(1, current_comic_number)


def download_random_comic():
    comic_number = get_random_comics_number()
    comic_url = f'https://xkcd.com/{comic_number}/info.0.json'
    response = requests.get(comic_url)
    response.raise_for_status()

    response = response.json()
    comic_comment = response['alt']
    download_comic_url = response['img']

    response = requests.get(download_comic_url)
    response.raise_for_status()
    with open(f'{directory}comic.png', 'wb') as comic_file:
        comic_file.write(response.content)

    return comic_comment

if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
