import asyncio
import aiohttp
import sys
import json

try:
    threads = int(sys.argv[1])
except IndexError:
    threads = 4

# Opera GXのアカウントトークンをここに入れよ
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhOThlNmNmZC0yYmE3LTQ3MDAtYjZkNy0wOTIzNDBhMjIzYjQiLCJleHAiOjE3MDkyOTU3MDF9.JYBmMg-_WsZYBjkrhnaMMBnmW6AMQqfnC1fWiRhAMZLBLKLYvnafAcZPVfBHdTbCTobQ8kaU3BE6GF672iBnfeikEJ0qj5sEAZVkbyHll3ySU3rUiuDbT2mQl9nwrDu_rJg8z-TduufZlxKVcdu3x1q3sVUpZRUGvC07hEGusg-nt1ChLWVuBz_4dRT4WVblNH95hR25T8lG-0DD3Ln1aiwbAhX6uggH4zQGhKGeiPIVxVP7COx_-8gaCd7NAPeH62jnvGjD5-EJ9EJp1NkseL7EdmebZufObVJ8IXjKgRQzBzCpOwP_3h3uNFydrFAReHSD4-ILf0I8FJzHYsDk_yIrCTbP-9YOrgaprov0GfQeghomZUsxtt8r0oqAmujZ_K8ndvhRRu735rru_BMcAGTIIzym3fpOH4LUEQwGab55RYykPzHQG3VzOsSNQbnng5dWTRALiFh9J4LzoaH31JIm0Y8T-xi_AvtA5VCNYglBFnzJrDGIOH0E8zBpgv_NST8P_AMyBrbTbYeDQf4K15c1xpf7JkQyx4kSaBCPDEB7QPZvAi_wDOgA-ait2Zt_Q0O7OylK624NvepAUOiQLmEDlmFjrAPwOzlzJFmX1eybmsKx0WFNYC7H5U6avnBqEJLFKjtugw1E2VjxEFPNPUNI4gB-5adjN_BoTUqLWyg"

headers = {
    'authority': 'discord.opr.gg',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': token,
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


async def runner():
    while True:
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.post("https://discord.opr.gg/v2/direct-fulfillment") as r:
                    if r.status == 200:
                        res = json.loads(await r.text())
                        promo_url = f"https://discord.com/billing/partner-promotions/1180231712274387115/{res['token']}"
                        with open("promos.txt", "a") as f:
                            f.write(f"{promo_url}\n")
                        print(f"[ \x1b[32mOK\x1b[0m ] {promo_url}")
                    elif r.status == 429:
                        print("[ \x1b[31mFAILED\x1b[0m ] レート制限がっ")
                    else:
                        print("[ \x1b[31mFAILED\x1b[0m ] 知らないエラーだ")
        except Exception as e:
            print(f"[ \x1b[31mFAILED\x1b[0m ] 知らないエラーだ {e}")


async def main():
    i = 0
    coroutines = []
    while i < threads:
        coroutines.append(runner())
        i += 1
    await asyncio.gather(*coroutines)

asyncio.run(main())
