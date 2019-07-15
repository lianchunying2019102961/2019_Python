# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:12:22 2019

@author: ASUS
"""
#生成数据
import random
import string
class Generate:
    def dic(self):
        dict={}
        u=''.join(random.sample(string.ascii_lowercase, 5))
        #返回包含所有小写字母在内的字符串
        v=''.join(random.sample(string.ascii_letters + string.digits, 6))  
        #返回包括所有字母在内的大小写字符串和0-9数字字符串
        dict[u]=v#生成字典
        return dict
    def string(self):
        s=''.join(random.sample(string.ascii_letters,6))
        #生成字符串
        return s
    def data_crecte(self,size=100000):
        data={}
        for i in range(size):
          data["int"]=random.randint(0,2000)
          #生成0-2000的随机整数
          data["float"]=random.uniform(3000,5000)
          data["dic"]=self.dic()
          data["string"]=self.string()
          #生成的字典包含整形，浮点，字符串，字典
          yield data#生成数据
if __name__ == '__main__':
    f = open("output.txt", "w")
    for i in Generate().data_crecte():
       s=str(i)
       f.write(s+'\n')
    f.close()