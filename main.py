import argparse
import os
from urllib.parse import urlparse

import requests 
from dotenv import load_dotenv


def is_bitlink(token, url):
    parsed = urlparse(url)
    retrieve_url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed.netloc}{parsed.path}/clicks/summary'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(retrieve_url, headers=headers)

    return response.ok

def count_clicks(token, link):
    parsed = urlparse(link)  
    summary_url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed.netloc}{parsed.path}/clicks/summary'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    payload = {
        'unit': 'day',
        'units': -1
    }

    response = requests.get(summary_url, headers=headers, params=payload)
    response.raise_for_status()

    return response.json()['total_clicks']

def shorten_link(token, url):
    shorten_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    payload = {
        'long_url':url
    }

    response = requests.post(shorten_url, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()['link']

def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='Creates a short version of the given link. For the short link - fetches total clicks.')
    args = parser.parse_args()

    access_token = os.getenv('BITLY_ACCESS_TOKEN')
    input_url = args.link

    if is_bitlink(access_token, input_url):
        try:
            clicks = count_clicks(access_token, input_url)
            print('Click count:', clicks)
        except requests.exceptions.HTTPError as err:
            print(err)     
    else:
        try:
            bitlink = shorten_link(access_token, input_url)
            print('Bitlink:', bitlink)
        except requests.exceptions.HTTPError as err:
            print(err)

if __name__ == '__main__':
    main()
  
