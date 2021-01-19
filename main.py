import logging
import os
import requests
import argparse
from urllib import parse

from dotenv import load_dotenv

logging.basicConfig(level=logging.ERROR)


def shorten_link(token, long_url):
    headers = {
        'Authorization': 'Bearer {}'.format(token),
        'Content-Type': 'application/json'
    }
    json_data = {
        'long_url': long_url,
        'domain': 'bit.ly',
    }

    url = 'https://api-ssl.bitly.com/v4/bitlinks'

    response = requests.post(url, headers=headers, json=json_data)
    response.raise_for_status()
    logging.info(response.json())
    bitlink = response.json()['id']
    return bitlink


def count_clicks(token, link):
    headers = {
        'Authorization': 'Bearer {}'.format(token),
    }
    params = {
        'unit': 'month',
        'units': '-1',
    }

    url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    url = url_template.format(bitlink=link)

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    logging.info(response.json())
    clicks_count = response.json()['total_clicks']
    return clicks_count


def retrieve_bitlink(token, link):
    headers = {
        'Authorization': 'Bearer {}'.format(token),
    }

    url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    url = url_template.format(bitlink=link)
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.getenv("BITLY_TOKEN")

    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='link to shorten or the bitly link')
    args = parser.parse_args()
    user_input = args.url
    logging.info(user_input)
    parsed_user_input = parse.urlparse(user_input)
    user_link = '{}{}'.format(parsed_user_input.netloc, parsed_user_input.path)

    if retrieve_bitlink(bitly_token, user_link):
        try:
            clicks_count = count_clicks(bitly_token, user_link)
            print('Count of clicks on the link:', clicks_count)
        except requests.exceptions.HTTPError:
            print('Error in determining the number of clicks')
    else:
        try:
            bitlink = shorten_link(bitly_token, user_input)
            print('Shortened link', bitlink)
        except requests.exceptions.HTTPError:
            print('Error getting a short link')


if __name__ == '__main__':
    main()
