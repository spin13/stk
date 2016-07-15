#-*- encoding:utf-8 -*-

from datetime import datetime, timezone, timedelta
import time


PRICE_FILE = './datas/prices/'

def get_nowtime():
    now = datetime.now()
    ret = str(now.year) + ' ' + str(now.month) + ' ' + str(now.day) + ' ' + str(now.hour) + ' ' + str(now.minute) + ' ' + str(now.second)
    return ret


def write_price(code, data):
    f = open(PRICE_FILE+code, 'a')
    now = get_nowtime()
    f.write(now + ' ' + str(data) + "\n")
    f.close()
    return True


print(get_nowtime())
