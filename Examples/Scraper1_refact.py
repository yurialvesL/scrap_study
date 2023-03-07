from urllib.request import urlopen
from urllib.error import URLError,HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'lxml')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle('http://pythonscraping.com/pages/page1.html')

if title is None:
    print('Tag not found!')
else:
    print(title)