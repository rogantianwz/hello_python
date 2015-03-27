#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys

if  __name__=='__main__':
    name = raw_input("please input name:")
    #print "hello: %s" % (name) #类似与c里面的print.format
    #print "hello: " + name #最常用的
    #print "hello: ", name 此种方式在两个字符串中间会多一个空格
    #print ''.join(["hello ",name]) 
    print ' '.join(["hello",name]) #对于S.jon(iterable),分隔符是S 
