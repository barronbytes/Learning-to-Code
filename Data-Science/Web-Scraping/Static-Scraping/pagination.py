from bs4 import BeautifulSoup as bs
from bs4.element import Tag


class Pagination():


    @staticmethod
    def calc_page_count(soup: bs) -> int:
        parent_tag = soup.select_one("ul.pagination")
        anchors = parent_tag.select("a.page-link")
        return int(anchors[-2].text)


    @staticmethod
    def scrape_products(soup: bs) -> list[str]:
        products = soup.select("a.title")
        return [p.text.strip() for p in products]


    @staticmethod
    def scrape_prices(soup: bs) -> list[str]:
        parent_tags = soup.select("div.caption")
        price_tags = [pt.select_one("span[itemprop='price']") for pt in parent_tags] # cannot use span.price !!!
        return [pt.text.strip() for pt in price_tags]
