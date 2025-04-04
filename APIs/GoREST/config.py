import os


BASE_URL = "https://gorest.co.in/"
BASE_PATH = "public/"
VERSION = "v2/"
ENDPOINT = "users/"


def get_request_url():
    return BASE_URL + BASE_PATH + VERSION + ENDPOINT


def get_headers():
    token = os.getenv("API_GOREST")
    return { "Authorization": f"Bearer {token}" }
