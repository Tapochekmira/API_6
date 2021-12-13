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


def get_upload_server_url(group_id, vk_token):
    upload_url = 'https://api.vk.com/method/photos.getWallUploadServer'
    payload = {
        'group_id': group_id,
        'access_token': vk_token,
        'v': '5.131'
    }
    response = requests.get(upload_url, params=payload)
    check_status(response)

    return response.json()['response']['upload_url']


def upload_comic_to_server(group_id, vk_token, directory):
    upload_server_url = get_upload_server_url(group_id, vk_token)
    with open(f'{directory}comic.png', 'rb') as file:
        files = {
            'file1': file,
        }
        response = requests.post(upload_server_url, files=files)
        check_status(response)
    response = response.json()
    return response['server'], response['photo'], response['hash']


def save_comic_to_album(group_id, vk_token, server, photo, hash):
    save_comic_to_album_url = 'https://api.vk.com/method/photos.saveWallPhoto'
    payload = {
        'group_id': group_id,
        'server': server,
        'photo': photo,
        'hash': hash,
        'access_token': vk_token,
        'v': '5.131'
    }
    response = requests.post(save_comic_to_album_url, params=payload)
    check_status(response)
    response = response.json()['response'][0]
    return response["owner_id"], response["id"]
if __name__ == '__main__':
    load_dotenv()
    vk_token = os.environ['ACCESS_TOKEN']
    group_id = os.environ['GROUP_ID']
    directory = 'images/'

    Path(directory).mkdir(parents=True, exist_ok=True)
    comic_comment = download_random_comic()

    server, photo, hash = upload_comic_to_server(group_id, vk_token, directory)

    owner_id, photo_id = save_comic_to_album(
        group_id,
        vk_token,
        server,
        photo,
        hash
    )
