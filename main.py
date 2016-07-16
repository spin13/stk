#-*- encodig:utf-8 -*-
import sys

sys.path.append('./Parse')
sys.path.append('./general_lib')

#import DataGetYahoo as gdata
import DataGetNikkei as gdata
import DataWrite as dw


def main():
    #datas = gdata.get_html(code)
    code1 = '7203'  # TOYOTA
    code2 = '7974'  # NINTENDO
    s1=gdata.get_html(code1)
    s2=gdata.get_html(code2)
    '''
    for i in open('./3765_nikkei.html', 'r'):
        s1 = s1+i
    for i in open('./2121_nikkei.html', 'r'):
        s2 = s2+i
    '''
    p1 = gdata.get_all_data(s1)
    p2 = gdata.get_all_data(s2)
    print(code1 + "\n" + str(p1))
    print()
    print(code2 + "\n" + str(p2))
    #dw.write_all('3765', p1)
    #dw.write_all('2121', p2)


if __name__ == '__main__':
    main()

