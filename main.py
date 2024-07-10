import json
import concurrent.futures

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

import platform_scripts.codeforces as cf
import platform_scripts.codechef as chef
import platform_scripts.leetcode as lt
import platform_scripts.codingninjas as ninja
from leetcode import contest

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the specific origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],  # Set this to the HTTP methods you want to allow
    allow_headers=["*"],  # Set this to the HTTP headers you want to allow
)

class NoCacheMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)
        cached = request.query_params.get('cached')
        if cached == 'false':  # TODO: add authentication for non-cached methods.
            response.headers['Cache-Control'] = 'no-store'
        return response

app.add_middleware(NoCacheMiddleware)


@app.get("/codeforces/{username}")
def get_codeforces_info(username: str):
    return cf.get_contest_data(username)


@app.get("/leetcode/{username}")
def get_leetcode_info(username: str):
    return lt.get_contest_data(username)


@app.get("/codechef/{username}")
def get_codechef_info(username: str):
    return chef.get_contest_data(username)


@app.get("/codingninjas/{username}")
def get_codingninjas_info(username: str):
    return ninja.get_contest_data(username)


@app.get("/{username}")
def get_all_ratings_from_username(username: str):
    with open('users.json') as file:
        users: dict = json.load(file)
        if username in users.keys():
            userdata = users[username]
        else:
            return {"error": "username not found!",
                    "code": 1100}

    body = {}
    sub_exec = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # TODO: for loop instead if statements
        if "leetcode" in userdata.keys():
            sub_exec['leetcode'] = executor.submit(lt.get_contest_data, userdata['leetcode'])
        if "codeforces" in userdata.keys():
            sub_exec['codeforces'] = executor.submit(cf.get_contest_data, userdata['codeforces'])
        if "codechef" in userdata.keys():
            sub_exec['codechef'] = executor.submit(chef.get_contest_data, userdata['codeforces'])
        if "codingninjas" in userdata.keys():
            sub_exec['codingninjas'] = executor.submit(ninja.get_contest_data, userdata['codingninjas'])
    concurrent.futures.wait(sub_exec.values())
    if "leetcode" in sub_exec.keys():
        body['leetcode'] = sub_exec['leetcode'].result()  # TODO: use better functions
    if "codeforces" in userdata.keys():
        body['codeforces'] = sub_exec["codeforces"].result()  # TODO: use better functions
    if "codechef" in userdata.keys():
        body['codechef'] = sub_exec["codechef"].result()  # TODO: function is ok but not complete
    if "codingninjas" in userdata.keys():
        body["codingninjas"] = sub_exec["codingninjas"].result()  # TODO: better functions

    return body


@DeprecationWarning
@app.get("/{username}/leetcode")
def get_leetcode_rating(username: str, cached: bool = True):
    if username[0] == "@":
        with open('users.json') as file:
            users: dict = json.load(file)
            if username not in users.keys():
                return {"error": "username not found!",
                        "code": 1100}
            if "leetcode" not in users[username].keys():
                return {"error": f"leetcode id for {username} not found!",
                        "code": 1101}
            username = users[username]['leetcode']
    return lt.get_contest_data(username)
