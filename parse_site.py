#!/usr/bin/env python
from BeautifulSoup import BeautifulSoup as BS
import urllib2
import sys

url = 'http://publico.pt'

webDownloader = urllib2.build_opener()
html = webDownloader.open(url)

soup = BS(html)

links = [link['href'] for link 
            in soup.findAll('a')
            if link.has_key('href')]
print links 
