import json
import requests
import time

base_url = "https://about-coderme.vercel.app/"
websites = {
    "leetcode": ["jayampatel"],
    "codeforces": ["jayampatel"]
}
status_data = {}

for website in websites:
    status_data[website] = []
    for testcase in websites[website]:
        endpoint = f"{base_url}{website}/{testcase}"
        response = requests.get(endpoint)
        status_data[website].append({
            "testcase": testcase,
            "status": "success" if response.status_code // 100 == 2 else "failure",
            "status_code": response.status_code,
        })

status_data = {
    "timestamp": time.time(),
    "data": status_data,
    "base_url": base_url
}

# Write the status data to api_status.json
with open("api_status.json", "w") as json_file:
    json.dump(status_data, json_file, indent=2)
