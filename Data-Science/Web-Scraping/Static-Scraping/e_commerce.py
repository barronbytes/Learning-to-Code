import requests
from bs4 import BeautifulSoup as bs
from pagination import Pagination


BASE_URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
r = requests.get(BASE_URL)
soup = bs(r.content, "lxml")
page_count = Pagination().calc_page_count(soup)
products = Pagination().scrape_products(soup)
prices = Pagination.scrape_prices(soup)
print(products)
print(prices)
