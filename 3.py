#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys

if  __name__=='__main__':
    #builtInNames = ['Alice','Bob'] #列表
    #builtInNames = ('Alice','Bob') #元组,数据不可变,更适合这里
    builtInNames = set(['Alice','Bob']) #set更适合这里,因为list,tuples的contains操作属于O(n),而set和dict的属于O(1)
    name = raw_input("please input name:")
    if(name in builtInNames):
        print ' '.join(["hello",name]) 
