import requests

from bs4 import BeautifulSoup


def get_contest_rating(username: str) -> int:
    response = requests.get(f"https://www.codechef.com/users/{username}")
    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        rating = soup.find("div", class_="rating-number").text.split("?")[0]
        return int(rating)


def get_contest_data(username: str, queries: list = None):
    pass
