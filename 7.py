#!/usr/bin/python
# _*_ coding:utf-8 _*_
#读文件

def read1():
    f = open("input/input-7", 'rU') # U:读取的时候所有形式的换行符全部转换为\n
    line = f.readline()
    while line:
        print line, #'comma' makes print without \n,后面跟逗号将忽略换行符
        #print line
        #print (line, end='') # 此写法为python3所用
        line = f.readline()
    f.close()

def read2():
    for line in open("input/input-7"):
        print line,

def read3():
    f = open("input/input-7")
    lines = f.readlines() #读取全部内容
    for line in lines:
        print line,
    f.close()

if __name__ == "__main__":
    read1()
    #read2()
    #read3()
