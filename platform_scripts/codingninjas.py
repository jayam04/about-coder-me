import requests
def get_uuid_from_username(username: str) -> str:
    response = requests.get(f"https://api.codingninjas.com/api/v3/public_section/profile/user_details?uuid={username}")
    return response.json()["data"]["uuid"]


def get_user_rating_data(uuid: str) -> dict:
    response = requests.get(f"https://api.codingninjas.com/api/v3/public_section/user_rating_data?uuid={uuid}")
    return response.json()['data']  # TODO: handle error, based on json()['error'] and more


def get_contest_data(username: str, queries: list = None):
    coding_ninjas_uuid = get_uuid_from_username(username)
    # TODO: if queries is none
    # TODO: tmp implementation it's not good as each function will scrape web all different times
    user_rating_data = get_user_rating_data(coding_ninjas_uuid)  # TODO: remove if not required ie, based on query
    return {
        "rating": int(user_rating_data['current_user_rating'])
    }
