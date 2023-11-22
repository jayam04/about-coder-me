# Endpoints

## 1. Using Endpoints
There are two main ways to access the data:  

### I. Using Claimed Username
`coderme.vercel.app/{claimed_username}`  

This uses the claimed username added to `users.json`.  
Can be used to get data for all platforms:
```
GET /{claimed_username}/
```

Or get platform specific data: 
```  
GET /{claimed_username}/{platform}
```

Works like a REST API - can append various paths to filter data.

### II. Using Platform Specific Username
`coderme.vercel.app/{platform}/{actual_username}`

This uses the actual username for a specific platform.

Can be used to get all data for that platform:
```
GET /{platform}/{actual_username} 
```

Can also apply queries to get partial data:
```
GET /{platform}/{actual_username}?query=query1+query2
```


## 2. Supported Platforms And Their Queries

|              | **leetcode** | **codeforces** | **codechef** |
|-------------:|:------------:|:--------------:|:------------:|
|  **website** | leetcode.com | codeforces.com | codechef.com |
|  **ratings** |    [yes]     |     [yes]      |    [yes]     |
| **contests** |    [yes]     |      [no]      |     [no]     |


[yes]: ✅  
[no]: ⭕  
