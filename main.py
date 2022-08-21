import requests
import json


def get_all_in_json(url):
    info = requests.get(url)
    if info.status_code == 200:
        return info.content
    else:
        return 'нет соединения'


def get_th_most_intelligence_hero(names, url):
    all_superheroes_data = json.loads(get_all_in_json(url))
    local_superhero_dict = []

    for superhero_data in all_superheroes_data:
        if superhero_data['name'] in names:
            local_superhero_dict.append([
                superhero_data["powerstats"]["intelligence"],
                superhero_data['name']])
    local_superhero_dict.sort(key=lambda x: -x[0])

    return local_superhero_dict[0][1]


if __name__ == '__main__':
    print("The most intelligence hero is ", end="")
    print(get_th_most_intelligence_hero(['Hulk', 'Captain America', 'Thanos'],
                                        "https://akabab.github.io/superhero"
                                        "-api/api//all.json"))
