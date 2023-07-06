import requests

get_endpoint = "http://localhost:8000/api/match/"

while True:
    get_response = requests.get(get_endpoint).json()
    matches = get_response["results"]
    data = {}
    for match in matches:
        data = {
            "club": match["club"],
            "season": match["season"],
            "num_matches_league": match["num_matches_league"],
            "num_matches_comps": match["num_matches_comps"],
            "league": 47,
        }
        update_endpoint = f"http://localhost:8000/api/match/update/{match['id']}/"
        update = requests.put(update_endpoint, json=data)
        print(update.json())

    if not get_response["next"]:
        break

    get_endpoint = get_response["next"]
