import re
import urllib
import urllib.request
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import json
import os
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


def soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    thepage.close()
    return soupdata


surl = "https://www.ansjewelry.com/shop?category=gold-coins"
soup1 = soup(surl)
print( soup1.)

card_inner = soup1.find_all(class_='card-title')
#print(card_inner.text)


for test1 in card_inner:
    print(test1.text)

