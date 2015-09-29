#!/usr/bin/python
# _*_ coding: utf-8 _*_
#求和

import sys

if  __name__=='__main__':
    n = raw_input("please input number:");
    while(not n.isdigit()):#str.isdigit()判断是不是都是数字,也可以使用n + 1的操作来看是否抛出异常来判断
        n = raw_input("please input number:")
    n = int(n)
    sum_num = 0
    #for i in range(1, n + 1):
    for i in range(n + 1): #start default 0, range's three type: range(end), range(start, end), range(start, end, step).note:exclude end
        sum_num = sum_num + i
    print "the sum is : %d" % (sum_num)
    
