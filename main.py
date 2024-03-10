import asyncio
import aiohttp
import requests
import sys
import json
import os
import random
from http.cookiejar import MozillaCookieJar

try:
    threads = int(sys.argv[1])
except IndexError:
    threads = 4

headers = {
    'authority': 'discord.opr.gg',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0',
}
cj = MozillaCookieJar('cookies.txt')
cj.load()
if os.path.exists("proxies.txt"):
    with open("proxies.txt", "r") as f:
        proxies = f.read().splitlines()
else:
    proxies = None


def generate_token():
    # aiohttpでCookieを使う方法が難解です
    r = requests.get("https://api.gx.me/profile/token", headers=headers, cookies=cj)
    token = r.json()["data"]
    headers["authorization"] = token


async def runner():
    while True:
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                if proxies:
                    proxy = random.choice(proxies)
                    r = await session.post("https://discord.opr.gg/v2/direct-fulfillment", proxy=proxy)
                else:
                    r = await session.post("https://discord.opr.gg/v2/direct-fulfillment")
                if r.status == 200:
                    res = json.loads(await r.text())
                    promo_url = f"https://discord.com/billing/partner-promotions/1180231712274387115/{res['token']}"
                    with open("promos.txt", "a") as f:
                        f.write(f"{promo_url}\n")
                    print(f"[ \x1b[32mOK\x1b[0m ] {promo_url}")
                elif r.status == 401:
                    print(f"[ INFO ] トークンが失効したぽいから再生成するぞ")
                    # トークン再生成
                    generate_token()
                    continue
                elif r.status == 403:
                    print("[ \x1b[31mFAILED\x1b[0m ] なぞのエラー")
                elif r.status == 429:
                    print("[ \x1b[31mFAILED\x1b[0m ] レート制限がっ")
                else:
                    print("[ \x1b[31mFAILED\x1b[0m ] 知らないエラーだ")
        except Exception as e:
            print(f"[ \x1b[31mFAILED\x1b[0m ] 知らないエラーだ {e}")


async def main():
    generate_token()
    i = 0
    coroutines = []
    while i < threads:
        coroutines.append(runner())
        i += 1
    await asyncio.gather(*coroutines)

asyncio.run(main())
