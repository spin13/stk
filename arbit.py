#-*- encoding:utf-8 -*-

import sys

sys.path.append('./Screening')
sys.path.append('./Parse')
sys.path.append('./general_lib')

import DataGetNikkei as gdata
import Arbitrage as arb

#DEMO_DIR = './datas/demo_price/'
DEMO_DIR = './datas/demo_price2/'
ALLOWED_DEVIATION = 10.0
ARBITRAGE_NETCHANGE = 5.0

def main():
    f = open('./input/arb_convenience.txt','r')
    symbol_list = []
    for i in f.readlines():
        symbol_list.append(i.strip())
    f.close()
    res = {}

    for i in symbol_list:
        f= open(DEMO_DIR + i, 'r')
        changes=[]
        for i2 in f.readlines():
            changes.append(float(i2.strip()))
        res.update({ i: arb.calc_total_changed(changes)})

    data_list = []
    for i in res.keys():
        data_list.append(res[i])
    diviation = arb.calc_standard_deviation(data_list)

    #print(diviation)
    print(res)
    chance = arb.check_arbitrage_chance(res, ALLOWED_DEVIATION, ARBITRAGE_NETCHANGE)
    print(chance)



if __name__ == '__main__':
    main()

