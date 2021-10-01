import requests
import json

with open("jsonFile/hero_ids.json", "rb") as f:
    hero_ids = json.load(f)

with open("jsonFile/item_ids.json", "rb") as f:
    item_ids = json.load(f)

r = requests.get("https://api.opendota.com/api/matches/6158010330/")
data = json.loads(r.content)


data = json.loads(r.content)
match_dict = {}
# print(hero_ids[str(data["players"][0]["hero_id"])])
for player in data["players"]:
    hero_info = {}
    account_id = player["account_id"]
    account_name = json.loads(requests.get(f"https://api.opendota.com/api/players/{account_id}/").content)["profile"][
        "personaname"]
    hero_id = player["hero_id"]
    hero_info["hero_name"] = hero_ids[str(hero_id)]
    hero_info["level"] = player["level"]
    hero_info["net_worth"] = player["net_worth"]
    hero_info["kills"] = player["kills"]
    hero_info["deaths"] = player["deaths"]
    hero_info["assists"] = player["assists"]
    hero_info["damage"] = player["hero_damage"]
    hero_info["items"] = []
    for i in range(6):
        hero_info["items"].append(item_ids[str(player[f"item_{i}"])])
    match_dict[account_name] = hero_info

print(match_dict)