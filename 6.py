#!/usr/bin/python
# _*_ coding: utf-8 _*_
#lambda表达式

import sys,random

def add_num(ret, n):
    ret += n
    return ret

def mult_num(ret, n):
    ret *= n
    return ret

print "abc"

if  __name__=='__main__':
    n = raw_input("please input number:");
    while(not n.isdigit()):
        n = raw_input("please input number:")
    n = int(n)
    if random.randrange(0,10) % 2 == 0:
		#需要import random模块,其中random.randint(a,b)函数include a和b,randrange exclude b
        #fun = add_num #使用变量前无须定义,add_num函数必须在之前定义,因为python会顺序执行这个脚本
        fun = lambda x, y : x + y
        ret = 0
        print("the algorithm is add")
    else:
        #fun = mult_num
        fun = lambda x, y : x * y # lambda表达式
        ret = 1
        print("the algorithm is mult")
    for i in range(1, n + 1):
        ret = fun(ret, i)
    print "the ret is : %d" % (ret)
    
