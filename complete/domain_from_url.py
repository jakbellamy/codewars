from src.test import test
import re

def domain_name(url):
    surl = re.split(r"[./]+", url)
    i = 0
    while not surl[i].find('http') == -1 or surl[i] == 'www': 
        i += 1
    return surl[i]

test(domain_name("http://google.com"), "google")
test(domain_name("http://google.co.jp"), "google")
test(domain_name("www.xakep.ru"), "xakep")
test(domain_name("https://youtube.com"), "youtube")

def _domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]