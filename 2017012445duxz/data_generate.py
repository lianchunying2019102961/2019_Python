﻿import random
import string
class Generate:
    def dic(self):
        dict={}
        k=''.join(random.sample(string.ascii_lowercase, 5))
        v=''.join(random.sample(string.ascii_letters + string.digits, 6))        
        dict[k]=v
        return dict
    def string(self):
        s=''.join(random.sample(string.ascii_letters,6))
        #生成字符串
        return s
    def data_crecte(self):
          data={}
          data["int"]=random.randint(0,2000)
          data["float"]=random.uniform(3000,5000)
          data["string"]=self.string()
          data["dic"]=self.dic()
         # yield data
          return data
if __name__ == '__main__':
    f = open("data.txt", "w")
    for i in range(100000):
       d=Generate().data_crecte()
       print(d)
       s=str(d)
       f.write(s+'\n')
    f.close()