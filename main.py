#-*- encodig:utf-8 -*-
import sys

sys.path.append('./Parse')
sys.path.append('./general_lib')

import DataGet as gdata
import DataWrite as dw


def main():
    #datas = gdata.get_html(code)
    s1=''
    s2=''
    for i in open('./3765.html', 'r'):
        s1 = s1+i
    for i in open('./2121.html', 'r'):
        s2 = s2+i
    p1 = gdata.scrape_price(s1)
    p2 = gdata.scrape_price(s2)

    dw.write_price('3765', p1)
    dw.write_price('2121', p2)


if __name__ == '__main__':
    main()

