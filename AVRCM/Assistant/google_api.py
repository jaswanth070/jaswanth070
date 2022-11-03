import requests
from bs4 import BeautifulSoup as bs

def GCF(query):
    try:
        headers = {
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.42 Safari/537.36",
            "Accept": "*/*",
            # "Referer": "https://www.cymath.com/answer?q=GCF{}".format(query),
            "Connection": "keep-alive",
        }

        params = {
            "q" : "%2024%2036",
        }

        r  = requests.get("https://www.cymath.com/answer", params=params)

        cookies = {
            "PHPSESSID": r.headers["Set-Cookie"].split("=")[1].split(";")[0],
        }

        params["lang"] = "en"

        # response = requests.get("https://www.cymath.com/ajax/get_steps.php/?q=GCF", headers=headers, params=params, cookies=cookies)
        response = requests.get("https://www.cymath.com/ajax/get_steps.php/?q=GCF%2024%2036",headers=headers,cookies=cookies)

        soup = bs(response.text,'html.parser')
        # res = soup.find('div',id='answer')
        print(response.url)
        return (soup.prettify())
    except:
        return None

def slove(query):
    try:
        headers = {
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.42 Safari/537.36",
            "Accept": "*/*",
            "Referer": "https://www.cymath.com/answer?q={}".format(query),
            "Connection": "keep-alive",
        }

        params = {
            # "q" : query,
            "q" : query,
        }

        r  = requests.get("https://www.cymath.com/answer", params=params)

        cookies = {
            "PHPSESSID": r.headers["Set-Cookie"].split("=")[1].split(";")[0],
        }

        params["lang"] = "en"

        response = requests.get("https://www.cymath.com/ajax/get_steps.php", headers=headers, params=params, cookies=cookies)

        soup = bs(response.text,'html.parser')
        res = soup.find('div',id='answer')
        print(response.url)
        # return (res.text)
        print(soup.prettify())
    except:
        return None

que = input()
res = slove(que)
# res = GCF(que)
print(res)
