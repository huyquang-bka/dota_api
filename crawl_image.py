import requests
import time
import json
from tqdm import tqdm

first_url = "https://cdn.cloudflare.steamstatic.com"


def download_image(name, url, folder):
    img_data = requests.get(first_url + url).content
    with open(f'{folder}/{name}.jpg', 'wb') as handler:
        handler.write(img_data)


def item_image():
    f = open("jsonFile/item.json", "r")
    data = json.load(f)

    item_name_list = list(data.keys())
    item_ids = dict()
    for item in tqdm(item_name_list):
        print(item)
        url = data[item]["img"]
        id = data[item]["id"]
        item_ids[id] = item
        # download_image(item, url, folder="Items")
        json_object = json.dumps(item_ids)

        # Writing to sample.json
        with open("jsonFile/item_ids.json", "w") as outfile:
            outfile.write(json_object)
    print("Done")


def heroes_image():
    f = open("jsonFile/heroes.json", "r")
    data = json.load(f)

    heroes_list = list(data.values())
    hero_ids = dict()
    for hero in tqdm(heroes_list):
        hero_name = hero["name"].split("hero_")[1]
        hero_id = hero["id"]
        hero_ids[hero_id] = hero_name
        # url = hero["img"]
        # download_image(hero_name, url, folder="Heroes")
    json_object = json.dumps(hero_ids)

    # Writing to sample.json
    with open("jsonFile/hero_ids.json", "w") as outfile:
        outfile.write(json_object)
    print("Done")


item_image()