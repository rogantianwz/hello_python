#!/usr/bin/python
# _*_ coding:utf-8 _*_
# 写文件

import sys,os

def write():
    f = open("output/output-8",'a') #mode 'a': append
    f.write("I'm American captain")
    f.write(os.linesep)
    f.write("Who are you")
    f.write(os.linesep) #os.linesep 表示系统换行符
    f.close()

if __name__ == '__main__':
    write()
