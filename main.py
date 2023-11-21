import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import platform_scripts.codeforces as codeforces
from leetcode import contest
from platform_scripts import codechef

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the specific origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],  # Set this to the HTTP methods you want to allow
    allow_headers=["*"],  # Set this to the HTTP headers you want to allow
)


@DeprecationWarning
@app.get("/{username}/leetcode/contest")
def get_leetcode_info(username: str):
    if username[0] != '@':
        return contest.get_contest_data(username)


@DeprecationWarning
@app.get("/{username}/leetcode/contest/basic")
def get_leetcode_info(username: str):
    return contest.get_contest_basic(username)


@DeprecationWarning
@app.get("/{username}/leetcode/contest/basic/rank")
def get_leetcode_rank(username: str):
    pass
    return contest.get_contest_rank(username)


@DeprecationWarning
@app.get("/{username}/leetcode/{query}")
def get_leetcode_info_based_on_query(username: str, query: str):
    query = query.split("+")
    pass
    return contest.get_leetcode_info(username, query)


@app.get("/codeforces/{username}")
def get_codeforces_info(username: str):
    return {
        "rating": codeforces.get_current_rating(username)
    }


@app.get("/leetcode/{username}")
def get_leetcode_info(username: str):
    return {
        "rating": contest.get_contest_basic(username)["data"]["userContestRanking"]["rating"]
    }


@app.get("/status")
def get_status():
    return json.load(open("status.json", "r"))


@app.get("/{username}")
def get_all_ratings_from_username(username: str):
    with open('users.json') as file:
        users: dict = json.load(file)
        if username in users.keys():
            userdata = users[username]
        else:
            return {"error": "username not found!",
                    "code": 1001}

    body = {}
    if "leetcode" in userdata.keys():
        body['leetcode'] = get_leetcode_info(userdata['leetcode'])  # TODO: use better functions
    if "codeforces" in userdata.keys():
        body['codeforces'] = get_codeforces_info(userdata['codeforces'])  # TODO: use better functions
    if "codechef" in userdata.keys():
        body['codechef'] = codechef.get_contest_rating(userdata['codeforces'])  # TODO: function is ok but not complete

    return body
