from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/{username}/leetcode/contest")
def get_leetcode_info(username: str):
    return contest.get_contest_data(username)

@app.get("/{username}/leetcode/contest/basic")
def get_leetcode_info(username: str):
    return contest.get_contest_basic(username)

@app.get("/{username}/leetcode/contest/basic/rank")
def get_leetcode_rank(username: str):
    pass
    return contest.get_contest_rank(username)

@app.get("/{username}/leetcode/{query}")
def get_leetcode_info_based_on_query(username: str, query: str):
    query = query.split("+")
    pass
    return contest.get_leetcode_info(username, query)
