from bs4 import BeautifulSoup, Tag
import requests

page = requests.get("https://personensuche.dastelefonbuch.de/Nachnamen-A").content
bs = BeautifulSoup(page, 'html.parser')

#Get name via ul + children
for elem in bs.find(class_='linklist').children:
    if type(elem) is Tag:
        print(elem.get_text())


#Get names via links/title
name_list = [name for name in bs.find_all('a') if name.has_attr('href') and 'Nachnamen' in name['href']]
for n in name_list:
    # name_parts = n['href'].split("/")
    # if name_parts[-1] == "Vornamen-Orte": print(name_parts[-2])
    # elif name_parts[-1] != "Nachnamen": print(name_parts[-1])
    print(n['title'])
