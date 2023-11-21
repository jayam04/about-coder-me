# about-coderme

API to access your leetcode rankings.  

![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fabout-coderme.vercel.app%2Fleetcode%2Fjayampatel&query=%24.rating&style=flat-square&label=leetcode)  
![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fabout-coderme.vercel.app%2Fcodeforces%2Fjayampatel&query=%24.rating&style=flat-square&label=codeforces)  

## Usage

Make `GET` request at `https://about-coderme.vercel.app/{website}/{username}/` for all data for that website  
For more see [URL Formatting](docs/endpoints.md)  

## Claim Your Username!!

It's not required but you can use it if you need multiple-platform requests (ex. leetcode + codeforces).  

### Steps

1. Create `fork`.
2. Add your username in `users.json` in format below:
    ```json
    {
    "USERNAME_YOU_NEED*": {
        "github": "YOUR_GITHUB_USERNAME*",
         "leetcode": "YOUR_LEETCODE_USERNAME",
         "codeforces": "YOUR_CODEFORCES_USERNAME"
   }
   }
   ```
   constraints:
   1. USERNAME_YOU_NEED (REQUIRED): username you need for your acm profile, must not be taken.  
   2. YOUR_GITHUB_USERNAME (REQUIRED): must match your current GitHub username for PR to be merged.
   3. others: optional
