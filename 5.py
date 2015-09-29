#!/usr/bin/python
# _*_ coding: utf-8 _*_
#求和，求余

import sys

if  __name__=='__main__':
    n = raw_input("please input number:");
    while(not n.isdigit()):
        n = raw_input("please input number:")
    n = int(n)
    sum_num = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum_num += i
    print "the sum is : %d" % (sum_num)
    
