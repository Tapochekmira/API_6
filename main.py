import os

import requests
from pathlib import Path
from random import randint
from dotenv import load_dotenv


def check_status(response):
    response.raise_for_status()
    if response.json().get('error'):
        raise requests.exceptions.HTTPError(response=response)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
