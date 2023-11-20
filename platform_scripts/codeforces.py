import requests


def get_current_rating(username):
    response = requests.get(f"https://codeforces.com/api/user.rating?handle={username}")
    data = response.json()
    return data["result"][-1]["newRating"]
