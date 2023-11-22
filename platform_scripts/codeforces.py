import requests


def get_current_rating(username: str):
    response = requests.get(f"https://codeforces.com/api/user.rating?handle={username}")
    data = response.json()
    return data["result"][-1]["newRating"]


def get_contest_data(username: str, queries: list = None):
    data = {}
    # TODO: if query is empty make all queries run
    data['rating'] = get_current_rating(username)
    return data
