#-*- encoding:utf-8 -*-

import sys

sys.path.append('./Screening')
sys.path.append('./Parse')

import DataGetNikkei as gdata
import Arbitrage as arb

DEMO_DIR = './datas/demo_price/'

def main():
    f = open('./input/arb_convenience.txt','r')
    symbol_list = []
    for i in f.readlines():
        symbol_list.append(i.strip())
    f.close()

    for i in symbol_list:
        print(i)
        f= open(DEMO_DIR + i, 'r')
        changes=[]
        for i2 in f.readlines():
            changes.append(float(i2.strip()))
        print(changes)
        print(arb.calc_total_changed(changes))
    res = {}




if __name__ == '__main__':
    main()

