# get stock price from Yahoo Finance by scraping
# required BeautifulSoup
# # yum install -y gcc libxml2 libxml2-devel libxslt libxslt-devel python-devel
# # pip install BeautifulSoup4
# # pip install lxml

#-*- coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup 

YAHOO_URL="http://stocks.finance.yahoo.co.jp/stocks/detail/?code="

# "code" is ticker symbol
def get_html(code):
    url = YAHOO_URL + code
    html = urllib.request.urlopen(url).read()
    return html


# get price from html source text
def scrape_price(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find_all("td", class_ = "stoksPrice")
    price = data[1].string.replace(",", "")
    return int(float(price))

# returns percentage of changed
def scrape_netchange(html):
    soup = BeautifulSoup(html, "lxml")

    # 0: no change
    # 1: up
    # 2: down
    changed = 0

    if soup.find("span", class_ = "icoUpGreen") :
        changed = soup.find("span", class_ = "icoUpGreen").string

    elif soup.find("span", class_ = "icoDownRed") :
        changed = soup.find("span", class_ = "icoDownRed").string
    changed = changed.replace('%', '')

    return float(changed.split('（')[1].split('）')[0])


def get_price(code):
    data = get_html(code)
    return scrape_price(data)


# get price changes up or down
def get_netchange(code):
    data = get_html(code)
    return scrape_netchange(data)

# arg: filename includes stock_code list(newline separated)
def get_price_list(filename):
    f = open(filename, 'r')
    l = f.readlines()
    code_list=[]
    for i in l:
        i=i.strip()
        if i:
            code_list.append(i)
    f.close()

    ret = {}
    for i in code_list:
        ret.update({i: get_price(i)})
    return ret

