import json
import requests

if __name__ == '__main__':
    page = requests.get('https://stackoverflow.com/questions/6386308/http-requests-and-json-parsing-in-python')
    print(page.text)
    # print(page.json())
    pass
