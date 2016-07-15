# get stock price from Yahoo Finance by scraping
# required BeautifulSoup
# # yum install -y gcc libxml2 libxml2-devel libxslt libxslt-devel python-devel
# # pip install BeautifulSoup4
# # pip install lxml

#-*- coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup 

URL="http://www.nikkei.com/markets/company/?scode="

# "code" is ticker symbol
def get_html(code):
    url = URL + code
    html = urllib.request.urlopen(url).read()
    return html


# get price from html source text
def scrape_price(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find_all("dd", class_ = 'stc-now')
    price = data[0].string.replace(',', '')
    return int(float(price))

# returns percentage of changed
def scrape_netchange(html):
    soup = BeautifulSoup(html, "lxml")

    changed = 0.0

    if soup.find("span", class_ = "cmn-plus stc-percent") :
        changed = soup.find("span", class_ = 'cmn-plus stc-percent').string
        changed = changed.replace('＋', '+')
    elif soup.find("span", class_ = "cmn-minus stc-percent") :
        changed = soup.find("span", class_ = 'cmn-minus stc-percent').string
        changed = changed.replace('－', '-')
    else:
        return 0.0
    changed = changed.replace('％', '')
    return float(changed.split('(')[1].split(')')[0])


def scrape_volume(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find_all("div", class_ = 'm-st-top_price_detail_list_value')
    return data[3].string.strip().replace(',', '').replace('株', '')


def scrape_PBR(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find_all("div", class_ = 'm-st-top_price_detail_list_value')
    return data[4].string.strip().replace('倍', '')


def scrape_PER(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find_all("div", class_ = 'm-st-top_price_detail_list_value')
    return data[5].string.strip().replace('倍', '')


# get the stock price
def get_price(code):
    data = get_html(code)
    return scrape_price(data)


# get price changes up or down
def get_netchange(code):
    data = get_html(code)
    return scrape_netchange(data)

def get_volume(code):
    data = get_html(code)
    return scrape_netchange(data)

def get_PBR(code):
    data = get_html(code)
    return scrape_netchange(data)

def get_PER(code):
    data = get_html(code)
    return scrape_netchange(data)


# arg: filename includes stock_code list(newline separated)
def get_all_data(code):
    #html = get_html(code)
    html = code
    ret ={}
    ret.update({'price': scrape_price(html)})
    ret.update({'netchange': scrape_netchange(html)})
    ret.update({'volume': scrape_volume(html)})
    ret.update({'PBR': scrape_PBR(html)})
    ret.update({'PER': scrape_PER(html)})
    return ret

