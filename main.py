import requests
import time
import random

TOKEN = "token"
DELAY = 2 # u can change this to wtv maybe dont go below 0.1 idk

guild_ids = [
    "123456789",
]


headers = {
    'accept': '*/*',
    'accept-language': 'en-GB',
    'authorization': TOKEN,
    'content-type': 'application/json',
    'origin': 'https://discord.com',
    'priority': 'u=1, i',
    'referer': 'https://discord.com/channels/',
    'sec-ch-ua': '"Not?A_Brand";v="99", "Chromium";v="130"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9188 Chrome/130.0.6723.191 Electron/33.4.0 Safari/537.36',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-GB',
    'x-discord-timezone': 'Europe/London',
}

while True:
    random.shuffle(guild_ids)
    for id in guild_ids:
        response = requests.put('https://discord.com/api/v9/users/@me/clan', headers=headers, json={"identity_guild_id": id, "identity_enabled": True})
        if response.status_code == 429:
            print("ratelimited lol")
            time.sleep(response.json()["retry_after"] or 30)
        else:
            time.sleep(DELAY)
