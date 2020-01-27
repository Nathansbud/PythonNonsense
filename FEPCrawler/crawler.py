from bs4 import BeautifulSoup
from requests import get
import os
from urllib.request import urlopen, Request

link = "https://freeexampapers.com/exam-papers/IB/Economics/Higher/"
tree = BeautifulSoup(get(link).content, 'html.parser')
if not os.path.exists(os.path.dirname(__file__) + os.sep + "output"):
    os.mkdir(os.path.dirname(__file__) + os.sep + "output")
for folder in tree.find_all("a")[5:]:
    page = BeautifulSoup(get(link + folder.get('href')).content, 'html.parser')
    if not os.path.exists(f"output/{folder.get('href')}"):
        os.mkdir(f"output/{folder.get('href')}")
    for pdf in page.find_all("a")[5:]:
        req = Request(link + folder.get('href') + pdf.get('href'), headers={'User-Agent': "Mozilla/5.0"})
        doc = urlopen(req)
        with open(f"output/{folder.get('href')}/{pdf.get('href')}", 'wb') as f:
            f.write(doc.read())
