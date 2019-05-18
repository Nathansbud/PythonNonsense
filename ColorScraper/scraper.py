from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup, SoupStrainer
import os
import json

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                print(resp.status_code)
                return None
    except RequestException as e:
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return resp.status_code == 200 and content_type is not None and content_type.find('html') > -1


def scrape_colors():
    page = BeautifulSoup(simple_get("https://en.wikipedia.org/wiki/List_of_colors_(compact)"), parse_only=SoupStrainer(attrs={'class':'mw-parser-output'}), features="html.parser")
    colors = {}
    for elem in page:
        for n in elem.findChildren('div'):
            m = n.findChildren('p')
            if len(m) == 2:
                colors.__setitem__(str(m[1].text), str(m[0].get('title')[m[0].get('title').find("𝗛𝗘𝗫")+5:]))
    print(colors)
    with open("data" + os.sep + "colors.json", "w+") as color_file:
        json.dump(colors, color_file)


if __name__ == "__main__":
    scrape_colors()
    pass