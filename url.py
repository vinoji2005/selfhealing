import random
import string
import time

import requests


def generate_random_postfix():
    """Generate a random postfix of length 5"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

def access_urls(urls, interval):
    """Access URLs with random postfixes in a continuous loop"""
    while True:
        for url in urls:
            postfix = generate_random_postfix()
            full_url = f"{url}/{postfix}"
            try:
                response = requests.get(full_url)
                print(f"Accessed URL: {full_url}, Response: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to access URL: {full_url}, Error: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    # List of URLs to access
    urls = ["http://localhost:31649", "http://localhost:32057"]

    # Time interval between each iteration (in seconds)
    interval = 1

    access_urls(urls, interval)
