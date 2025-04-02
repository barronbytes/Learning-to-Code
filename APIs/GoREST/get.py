import requests
import config


r = requests.get(config.get_request_url())
print(r.status_code)
