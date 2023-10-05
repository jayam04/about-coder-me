import requests

url = 'https://leetcode.com/graphql/'
headers = {
    'authority': 'leetcode.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.6',
    'authorization': '',
    'baggage': 'sentry-environment=production,sentry-release=9d738d6a,sentry-transaction=%2Fu%2F%5Busername%5D,sentry-public_key=2a051f9838e2450fbdd5a77eb62cc83c,sentry-trace_id=7d8a7cbd2ef14a29bffbd9324692b0a3,sentry-sample_rate=0.03',
    'content-type': 'application/json',
    'origin': 'https://leetcode.com',
    'random-uuid': '71e58adf-6e03-061b-50be-e43501dd5f84',
    'referer': 'https://leetcode.com/jayampatel/',
    'sec-ch-ua': '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'sentry-trace': '7d8a7cbd2ef14a29bffbd9324692b0a3-b931d8fdfccff382-0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-csrftoken': 'SHnPcpGqeYXA9VWDCBtOARZsKnAZPqE8ZgslpCho4zKiQHj28C25fkYqWimH7I1G',
}

def get_contest_data(username: str):
    """
    Get contest data
    :param username:
    :return:
    """

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
        "variables": {"username": username},
        "operationName": "userContestRankingInfo"
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

def get_contest_basic(username: str):
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
            }
        """,
        "variables": {"username": username},
        "operationName": "userContestRankingInfo"
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()
