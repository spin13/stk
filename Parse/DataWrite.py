#-*- encoding:utf-8 -*-

from datetime import datetime, timezone, timedelta
import time


FILE_PRICE= './datas/prices/'
FILE_NETCHANGE = './datas/netchange/'
FILE_VOLUME = './datas/volume/'
FILE_PBR = './datas/PBR/'
FILE_PER = './datas/PER/'

def get_nowtime():
    now = datetime.now()
    ret = str(now.year) + ' ' + str(now.month) + ' ' + str(now.day) + ' ' + str(now.hour) + ' ' + str(now.minute) + ' ' + str(now.second)
    return ret


def write(filename, data, now):
    f = open(filename, 'a')
    f.write(now + ' ' + str(data) + "\n")
    f.close()

def write_all(code, data):
    now = get_nowtime()
    write(FILE_PRICE+code, data['price'], now)
    write(FILE_NETCHANGE+code, data['netchange'], now)
    write(FILE_VOLUME+code, data['volume'], now)
    write(FILE_PBR+code, data['PBR'], now)
    write(FILE_PER+code, data['PER'], now)
    return True



