import os


BASE_URL = "https://gorest.co.in/"
BASE_PATH = "public/"
VERSION = "v2/"
USERS = "users/"


def get_access_token():
    return os.getenv("API_GOREST")


def get_request_url():
    return BASE_URL + BASE_PATH + VERSION + USERS
