import requests
from pprint import pprint
import json

def get_all_in_json(url):
    info = requests.get(url)
    pprint(info)
    if info.status_code == 200:
        return info.content
    else:
        return 'нет соединения'


if __name__ == '__main__':
    all_superheroes_data = json.loads(get_all_in_json(
        "https://akabab.github.io/superhero-api/api//all.json"))
    pprint(all_superheroes_data)
    with open('1.txt', 'w+') as f:
        json.dump(all_superheroes_data, f, indent=2)
