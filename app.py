from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

with open("jsonFile/hero_ids.json", "rb") as f:
    hero_ids = json.load(f)

with open("jsonFile/item_ids.json", "rb") as f:
    item_ids = json.load(f)


@app.route("/")
def first_page():
    return "This is for Dota Api"


@app.route("/match_info/<match_id>")
def match_info(match_id):
    r = requests.get(f"https://api.opendota.com/api/matches/{match_id}/")
    data = json.loads(r.content)
    match_dict = []
    count = 0
    for player in data["players"]:
        hero_info = {}
        account_id = player["account_id"]
        account_name = json.loads(requests.get(f"https://api.opendota.com/api/players/{account_id}/").content)["profile"]["personaname"]
        hero_info[f"playername"] = account_name
        hero_id = player["hero_id"]
        hero_info[f"heroname"] = hero_ids[str(hero_id)]
        hero_info[f"level"] = player["level"]
        hero_info[f"networth"] = player["net_worth"]
        hero_info[f"kills"] = player["kills"]
        hero_info[f"deaths"] = player["deaths"]
        hero_info[f"assists"] = player["assists"]
        hero_info[f"damage"] = player["hero_damage"]
        hero_info[f"items"] = []
        for i in range(6):
            hero_info[f"items"].append(item_ids[str(player[f"item_{i}"])])
        match_dict.append(hero_info)

    return jsonify(match_dict)


if __name__ == "__main__":
    app.run(debug=True)

