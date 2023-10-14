import json
import requests
import time
import re

base_url = "https://about-coderme.vercel.app/"
websites = {
    "leetcode": ["jayampatel", "hasan_15_07_03"],
    "codeforces": ["jayampatel"]
}
status_data = {}

# Get the status of each website
for website in websites:
    status_data[website] = []

    # Get the status of each testcase for each website
    for testcase in websites[website]:
        endpoint = f"{base_url}{website}/{testcase}"
        response = requests.get(endpoint)
        status_data[website].append({
            "testcase": testcase,
            "status": "success" if response.status_code // 100 == 2 else "failure",
            "status_code": response.status_code,
        })

    # Update the status badge in the README.md file
    with open("README.md", "r") as readme_file:
        readme_content = readme_file.read()

    avg_success = sum(1 for status in status_data[website] if status["status"] == "success") / len(status_data[website])
    status = "UP"  if avg_success >= 0.5 else "DOWN"
    color = "brightgreen" if avg_success > 0.7 else "red"
    readme_content = re.sub(r"!\[" + website + r"\]\(.*\)", f"![{website}](https://img.shields.io/badge/{website}-success%20rate:%20{int(avg_success * 100)}-{color})", readme_content)

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)


# Create the status data
status_data = {
    "timestamp": int(time.time()),
    "data": status_data,
    "base_url": base_url
}

# Write the status data to api_status.json
with open("api_status.json", "w") as json_file:
    json.dump(status_data, json_file, indent=2)
