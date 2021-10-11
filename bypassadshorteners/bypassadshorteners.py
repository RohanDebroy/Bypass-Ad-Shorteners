import json
import pathlib
from urllib.parse import urlparse

import requests

from bypassadshorteners.utils_crypto import decode_string

# * This global variable is used to keep track of how many times we have retried.
# *Basically a hacky method
retry_counter = 0


def load_config() -> dict:
    '''
    This function loads data from the config file else it calls the fetch config
    and then save the config.
    '''
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
    '''
    This function requests for the configuration like accepted domains
    and access key and other information and returns a json response. 
    '''
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
    '''
    This function is used to save all the config fetched from the server
    to a json file.

    It is used to retain data so that unnecessary calls to the server can be reduced. 
    '''
    try:
        with open(f'{pathlib.Path.cwd()}/config.json', mode='w', encoding='utf-8') as file:
            json.dump(data, file)
        return True
    except:
        return False


def fetch_request(url, access_key) -> dict:
    '''
    This function generates the headers and payload and send it
    along with the request and returns a json response
    '''
    headers = {
        'x-requested-with': 'XMLHttpRequest',
        'x-meow': 'me\xBAow',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    }

    data = {
        'l': url,
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
    '''
    A simple hack to retry my request for a total of 3 times
    This function calls the initlaize request with the url
    as params.
    '''
    global retry_counter
    retry_counter += 1

    if retry_counter > 3:
        return {"status": "failed"}

    return initalize_request(url)


def initalize_request(url: str) -> dict:
    '''
    This function after initialization passes the access key and the url
    to the fetch_request method which return the bypassed url.
    '''
    data = load_config()
    access_key = decode_string(data["access_key"])
    return fetch_request(url=url, access_key=access_key)


def is_url_supported(url: str) -> bool:
    '''
    This Function returns a boolean True if the url falls under supported category
    else False is returned.
    '''
    data = load_config()
    base_url = urlparse(url).netloc

    return base_url in data["diff_domains"] or base_url in data["accept_domains"]


def bypass_url(url: str) -> dict:
    '''
    This function calls the initlaize method by passing the url as params
    and returns a response.
    '''
    if is_url_supported(url):
        return initalize_request(url=url)
    else:
        return {"status": "Url unsupported"}


def recursive_bypass_url(url: str) -> dict:
    '''
    It calls bypass url underneath recursivelys i.e it will keep calling bypass url
    on the provided url for the first time and the responsed url from the 2nd time 
    unitl the actuall url is fetched.
    '''
    response = bypass_url(url)
    try:
        check_supported_url = is_url_supported(response["result"])
        if response["result"] != "":
            if check_supported_url == False:
                return response
            return recursive_bypass_url(response["result"])
    except:
        return response
