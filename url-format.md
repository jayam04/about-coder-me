# URL Format

## Intro

Current to access API, base url will be `https://about-coderme.vercel.app/{username}/` where username will be your username for specific site.  
Above URL will have all data from `/{username}/*`, where * is used for platform like leetcode (only one currently supported).  
There is issue of users having different usernames across different platforms and we will try to find good solution to it.  

## Leetcode

For leetcode you can use `/{username}/leetcode` to get all profile data of leetcode.

Currently additional URLs are `{uname}/leetcode/contest` giving data only about content (with contest history).  
and other `{uname}/leetcode/contest/basic` for contest data (without contest history).  
