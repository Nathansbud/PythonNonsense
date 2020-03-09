from bs4 import BeautifulSoup
from requests import get
import os
from urllib.request import urlopen, Request

courses = [
    # {"course":"English A Language and literature", "level":"SL", "group":1},
    # {"course":"Spanish B", "level":"SL", "group":2},
    # {"course":"Economics", "level":"HL", "group":3},
    # {"course":"Computer science", "level":"HL", "group":4},
    # {"course":"Physics", "level":"HL", "group":4},
    {"course":"Mathematics", "level":"HL", "group":5},
]

def classes_with_group(group, course_set):
    classes = []
    for c in course_set:
        if c['group'] == group: classes.append(c)
    return classes

link = "https://www.ibdocuments.com/IB%20PAST%20PAPERS%20-%20SUBJECT/"
tree = BeautifulSoup(get(link).content, 'html.parser')
group_links = [a.get('href') for a in tree.find_all("a") if a.get('href') and a.get('href').startswith("Group")][::2]
for group_link in group_links:
    name = group_link.replace("%20", " ")
    classes_in_group = classes_with_group(int(name[6]), courses)
    if classes_in_group:
        for c in classes_in_group:
            course_page = BeautifulSoup(get(link+group_link+c['course'].replace(" ", "_")+"_"+c['level']+"/").content, 'html.parser')
            mkpath = os.path.join(os.path.dirname(__file__), "output", c['course'].title())
            if not os.path.exists(mkpath):
                os.mkdir(mkpath)
            session_pages = [a.get("href") for a in course_page.find_all("a") if a.get("href") and a.get("href").endswith("Session/")][::2]
            for s in session_pages:
                session_page = BeautifulSoup(get(link+group_link+c['course'].replace(" ", "_")+"_"+c['level']+"/"+s).content, 'html.parser')
                mkpath = os.path.join(os.path.dirname(__file__), "output", c['course'].title(), s.replace("%20", " "))
                if not os.path.exists(mkpath):
                    os.mkdir(mkpath)
                pdfs = [a.get("href") for a in session_page.find_all("a") if a.get("href") and a.get("href").endswith(".pdf")][::2]
                for pdf in pdfs:
                    req = Request(link+group_link+c['course'].replace(" ", "_")+"_"+c['level']+"/"+s+pdf, headers={'User-Agent': "Mozilla/5.0"})
                    doc = urlopen(req)
                    with open(os.path.join(mkpath, pdf), 'wb') as f: f.write(doc.read())
                    print(f"Downloaded {link+group_link+c['course'].replace(' ', '_')+'_'+c['level']+'/'+s+pdf}")
