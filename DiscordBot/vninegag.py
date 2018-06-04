### Script for getting source and name from new article on 9gag.com

import urllib
import requests

ninegag = "http://9gag.com/"
### This is how script recognize new article.
wwsf='"position":1,"url":"https:\/\/9gag.com\/gag\/'
iasf='https://img-9gag-fun.9cache.com/photo/'

def exists(url, file):
    conn = httplib.HTTPConnection(url)
    conn.request('HEAD', file)
    response = conn.getresponse()
    conn.close()
    return response.status == 200

def page_to_str(url):
    a = urllib.request.urlopen(url)
    enc = a.headers.get_content_charset("utf-8")
    d = a.read()
    return d.decode(enc)

### Getting link of gag from 1st position
def get_gag():
    b = page_to_str(ninegag)
    c = b.find(wwsf)+45
    ce= len(b)-c-7
    gag = b[c:-ce]
    return ninegag+"gag/"+gag

### Returning title as a string.
def get_title(url):
    b = page_to_str(url)
    c = b.find("<title>")+7
    d = len(b)-b.find("</title>")+7
    return str("[ "+b[c:-d]+" ]").replace("&#039;","'")

### Returning link to content (gif/photo/video) as a string.
def get_url(url):
    gag = url[20:]
    check = iasf+gag+"_460svvp9.webm"
    r = requests.get(check)
    if r.status_code == 200:
        return check
    else:
        return iasf+gag+"_700bwp.webp"