import requests
from bs4 import BeautifulSoup as bs
from bs4.element import Tag


URL = "https://quotes.toscrape.com/"
r = requests.get(url=URL)
soup = bs(r.content, "lxml")
results = soup.find_all("div", attrs={"class":"quote"})

def scrape_by_find(results: list[Tag]) -> None:
    for result in results:
        quote = result.find("span", attrs={"class":"text"}).text
        author = result.find("small", attrs={"class":"author"}).text
        print(f"{author} said: {quote}\n")


def scrape_by_selector(results: list[Tag]) -> None:
    for result in results:
        quote = result.select_one("span.text").text
        author = result.select_one("small.author").text
        print(f"{author} said: {quote}\n")


#scrape_by_find(results)
#scrape_by_selector(results)


""" OBJECTS
1. Soup objects: <class 'bs4.BeautifulSoup'>

print(soup.name) # document

2. Tag objects: <class 'bs4.element.Tag'>

print(soup.span) # <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
print(soup.span.name) # span
print(soup.span["class"]) # ["text"]
print(soup.span.text) # text
"""