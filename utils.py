from utils_crypto import decode_string
from urllib.parse import urlparse
import requests
import pathlib
import json

retry_counter = 0

def load_config() -> dict:
    try:
        with open(f'{pathlib.Path.cwd()}/config.json', mode='r', encoding='utf-8') as file:
            data = json.load(file)
        
        if data == {}:
            raise Exception
        return data
    except:
        data = fetch_config()
        save_config(data)
        return data


def fetch_config() -> dict:
    headers = {
        'x-requested-with': 'XMLHttpRequest',
        'x-meow': 'me\xBAow'
    }
    try:
        with requests.get("https://api.yuumari.com/ex-alb/_/", headers=headers) as response:
            data = response.json()
        return data
    except:
        return {}


def save_config(data: dict) -> bool:
    try:
        with open(f'{pathlib.Path.cwd()}/config.json', mode='w', encoding='utf-8') as file:
            json.dump(data, file)
    except:
        return False

def fetch_request(url, access_key) -> dict:
    headers = {
        'x-requested-with': 'XMLHttpRequest',
        'x-meow': 'me\xBAow',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    }

    data = {
        'l':url,
        'u': access_key
    }

    try:
        with requests.post('https://api.yuumari.com/ex-alb/', headers=headers, data=data) as response:
            responseBody = response.json()

        if responseBody["result"] == "" and responseBody["message"] != "":
            raise Exception
        
        return responseBody
    
    except:
        pathlib.Path(f'{pathlib.Path.cwd()}/config.json').unlink()
        return retry_request(url)

def retry_request(url: str):
    global retry_counter 
    retry_counter+= 1
        
    if retry_counter > 3:
        return {"status":"failed"}

    return initalize_request(url)

def initalize_request(url: str) -> dict:
    data = load_config()
    access_key = decode_string(data["access_key"])
    return fetch_request(url=url, access_key=access_key)

def is_url_supported(url: str) -> bool:
    data = load_config()
    base_url = urlparse(url).netloc

    return base_url in data["diff_domains"] or base_url in data["accept_domains"]

def bypass_url(url: str) -> dict:
    if is_url_supported(url):
        return initalize_request(url=url)
    else:
        return {"status":"Url unsupported"}

def recursive_bypass_url(url:str) -> dict:
    response = bypass_url(url)
    try:
        check_supported_url = is_url_supported(response["result"])
        if response["result"] != "":
            if check_supported_url == False:
                return response
            return recursive_bypass_url(response["result"])
    except:
        return response
                

def main():
    # url = input("Enter the url to bypass : ")
    # bypass_url(url)
    url = "https://ouo.io/HOboAf"
    a = recursive_bypass_url(url)
    print(a)

if __name__ == '__main__':
    main()
