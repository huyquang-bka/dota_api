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
    match_dict = {}
    hero_info = {}
    count = 0
    for player in data["players"]:
        account_id = player["account_id"]
        account_name = json.loads(requests.get(f"https://api.opendota.com/api/players/{account_id}/").content)["profile"]["personaname"]
        hero_info[f"playername{count}"] = account_name
        hero_id = player["hero_id"]
        hero_info[f"heroname{count}"] = hero_ids[str(hero_id)]
        hero_info[f"level{count}"] = player["level"]
        hero_info[f"networth{count}"] = player["net_worth"]
        hero_info[f"kills{count}"] = player["kills"]
        hero_info[f"deaths{count}"] = player["deaths"]
        hero_info[f"assists{count}"] = player["assists"]
        hero_info[f"damage{count}"] = player["hero_damage"]
        hero_info[f"items{count}"] = []
        for i in range(6):
            hero_info[f"items{count}"].append(item_ids[str(player[f"item_{i}"])])
        # match_dict[count] = hero_info
        count += 1

    return jsonify(hero_info)


if __name__ == "__main__":
    app.run(debug=True)
