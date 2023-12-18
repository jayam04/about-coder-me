# About Coder Me 💻

## Overview 📘

API to access your competitive programming profiles and rankings across platforms like LeetCode and Codeforces.  

![LeetCode Rating](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fabout-coderme.vercel.app%2Fleetcode%2Fjayampatel&query=%24.rating&style=flat-square&label=LeetCode)  
![Codeforces Rating](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fabout-coderme.vercel.app%2Fcodeforces%2Fjayampatel&query=%24.rating&style=flat-square&label=Codeforces)  
![Codechef Rating](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcoderme.vercel.app%2Fcodechef%2Fjayampatel&query=%24.rating&style=flat-square&label=Codechef)  

## Usage 📱

Make a `GET` request to `https://about-coderme.vercel.app/{website}/{username}/` to retrieve data for a particular website.  

See [API Endpoints Doc](docs/endpoints.md) 📃 for more details on API endpoints.

## Claim Your Username!! 🎉 

You can claim a consistent username across platforms:

1. Fork this repo 🍴  
2. Add your details to database:
    1. Method 1 (better v2): Add to `users/{YOUR_GITHUB_USERNAME}.json`:

        ```json
        {
          "username": "YOUR_CHOSEN_USERNAME*1",
          "github": "YOUR_GH_USERNAME*1",
          "leetcode": "LEETCODE_UN",
          "codeforces": "CODEFORCES_UN",
          "codechef": "CODECHEF_UN",
          "codingninjas": "CODING_NINJAS_STUDIO_UN"
        }
        ```

        \*1 required fields  

    2. Method 2 (to be depreciated v1): Add to `users.json`

        ```json
        {
          "YOUR_CHOSEN_USERNAME": {  
            "github": "YOUR_GH_USERNAME",
            "leetcode": "YOUR_LEETCODE_USERNAME",
            "codeforces": "YOUR_CF_USERNAME" 
          }
        }
        ```

Constraints: 🚧

- `YOUR_CHOSEN_USERNAME`: Username you want to claim  
- `YOUR_GH_USERNAME`: Must match your GitHub username
- Others are optional, which are `codechef`, `codeforces`, `codingninjas`, `leetcode`, `linkedin` and `website`. For website provide full including http protocol url ex. `https://jayampatel.vercel.app`
