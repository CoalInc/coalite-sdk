import requests
import json
from types import SimpleNamespace


if __name__ == '__main__':
    url = 'https://lore.ketchup.pizza/coalite'
    resp = requests.get(url)
    coalite = json.loads(resp.text, object_hook=lambda d: SimpleNamespace(**d))