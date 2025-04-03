import requests
import config
import time


MAX_ATTEMPTS = 3
TIMEOUT = 1.2
request_url = config.get_request_url()


for i in range(1, MAX_ATTEMPTS+1):
    try:
        response = requests.get(request_url, timeout=TIMEOUT)
        data = response.json()
        break
    except (requests.exceptions.HTTPError, 
        requests.exceptions.Timeout, 
        requests.exceptions.RequestException, 
        ValueError) as e:
        print(f"Attempt {i} failed: {e}")


print(f"{data}")
