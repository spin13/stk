#-*- coding:utf-8 -*-



def calc_total_changed(changed_list):
    ret = 100.0
    for i in changed_list:
        ret = ret + (100.0*(i/100.0))
    return ret
