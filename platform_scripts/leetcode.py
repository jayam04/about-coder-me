import requests

data = {
    "query": """
        query userContestRankingInfo($username: String!) {
            userContestRanking(username: $username) {
                attendedContestsCount
                rating
                globalRanking
                totalParticipants
                topPercentage
                badge {
                    name
                }
            }
            userContestRankingHistory(username: $username) {
                attended
                trendDirection
                problemsSolved
                totalProblems
                finishTimeInSeconds
                rating
                ranking
                contest {
                    title
                    startTime
                }
            }
        }
    """,
    "variables": {"username": "jayampatel"},
    "operationName": "userContestRankingInfo"
}


def generate_query(pars_required: list):
    pass


def get_contest_data(username: str, queries: list = None):
    # TODO: tmp code to remove leetcode/contest.py
    data['variables']['username'] = username
    response = requests.post('https://leetcode.com/graphql/', json=data)
    if response.ok:
        response = response.json()
        return {
            "rating": round(response['data']['userContestRanking']['rating'])
        }
    pass
