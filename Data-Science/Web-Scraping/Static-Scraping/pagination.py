from bs4 import BeautifulSoup as bs


class Pagination():

    @staticmethod
    def calc_page_count(soup: bs) -> int:
        parent_tag = soup.find("ul", attrs={"class":"pagination"})
        anchors = parent_tag.select("a.page-link")
        return int(anchors[-2].text)