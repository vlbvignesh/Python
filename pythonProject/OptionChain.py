import requests
import json

#url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

optionindices = "NIFTY"


baseurl = "https://www.nseindia.com/"
if optionindices == "NIFTY":
    url = f"https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
else:
    url = f"https://www.nseindia.com/api/option-chain-equities?symbol="+optionindices+""
print(url)
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) '
                         'Chrome/80.0.3987.149 Safari/537.36',
           'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
session = requests.Session()
request = session.get(baseurl, headers=headers, timeout=5)
cookies = dict(request.cookies)




def fetchoi():
    response = session.get(url, headers=headers, timeout=5, cookies=cookies)
    print(response.json())
    with open("oi.json", "w") as files:
        files.write(json.dumps(response.json(), indent=4 , sort_keys=True))


def main():
    fetchoi()

if __name__ == '__main__':
    main()

