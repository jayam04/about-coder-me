# About Coder Me 💻

## Overview 📘

API to access your competitive programming profiles and rankings across platforms like LeetCode and Codeforces.  

![LeetCode Rating](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fabout-coderme.vercel.app%2Fleetcode%2Fjayampatel&query=%24.rating&style=flat-square&label=LeetCode)  
![Codeforces Rating](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fabout-coderme.vercel.app%2Fcodeforces%2Fjayampatel&query=%24.rating&style=flat-square&label=Codeforces)  

## Usage 📱

Make a `GET` request to `https://about-coderme.vercel.app/{website}/{username}/` to retrieve data for a particular website.  

See [API Endpoints Doc](docs/endpoints.md) 📃 for more details on API endpoints.

## Claim Your Username!! 🎉 

You can claim a consistent username across platforms:

1. Fork this repo 🍴  
2. Add your details to `users.json`:

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
- Others are optional, which are `codechef`, `codeforces` and `leetcode`
