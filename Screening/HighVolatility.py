# -*- encoding:utf-8 -*-

import BeautifulSoup as soup


# in volatility list
def get_average_volatility(vlist, period):
    l = vlist.reversed()
    ret = 0.0
    for i in l:
        ret += float(i)
    return ret/period
