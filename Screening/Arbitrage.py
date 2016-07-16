#-*- coding:utf-8 -*-

import math

def calc_total_changed(changed_list):
    ret = 100.0
    for i in changed_list:
        ret = ret + (100.0*(i/100.0))
    return ret


def calc_standard_deviation(data_list):
    avg = 0.0
    sum = 0.0
    for i in data_list:
        sum += i
    avg = sum/len(data_list)

    dist = 0.0
    # distribution
    for i in data_list:
        dist += ((i - avg) * (i - avg))
    return math.sqrt(dist)


# datalist expected DICTIONARY OBJECT
# //TODO
# currently return 2 symbols
# it will be some symbols to arbitrage
def check_arbitrage_chance(data_list, allowed, arb_chance):
    sorted_data = []
    for k, v in sorted(data_list.items(), key=lambda x:x[1]):
        sorted_data.append(k)

    ret = { 'long': [], 'short': []}
    gap = data_list[sorted_data[len(sorted_data)-1]] - data_list[sorted_data[0]]

    if arb_chance <= gap and gap <= allowed:
        ret['long'].append(sorted_data[len(sorted_data)-1])
        ret['short'].append(sorted_data[0])
    else:
        return None
    return ret
