
#随机生成整型、浮点型、字符串、字典
#导入MongoDB
#绘制散点图
import string
import random
from pymongo import MongoClient
import pandas as pd
import numpy as num
import matplotlib.pyplot as pl 


link = MongoClient('localhost')
hq = link.random_num 
start = hq.myrandom  
start.remove(None)

def Random(i):
    while i!=0:
        rand_str =  ''.join(random.sample(string.ascii_letters + string.digits,10))
        rand=random.randint(1,100000)
        key=random.choice(string.ascii_letters)
        dict1={key:rand}
        dict2={key:rand_str}
        tup1 = (rand_str,rand,dict1,dict2)
        yield tup1
        randomNumber = {
            '整型': rand,
            '字符': rand_str,
            '字典1': dict1,
            '字典2':dict2,

        }
        start.insert_one(randomNumber)
        i= i - 1
    return 'done'
h = Random(100000)
q = open("love.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(h)
        print(y, file = q)
    except StopIteration as a:
        print(a.value)
        break
q.close()

m = num.arange(1,100001)
client = pymongo.MongoClient('localhost', 27017)
hq = client['random_num']
table = hq['myrandom']

data = pd.DataFrame(list(start.find()))

n = data['整型']


fig = pl.figure()  
ax = fig.add_subplot(111)
ax.set_title('Scatter int') 
ax.scatter(m,n,c = 'g',marker = 'o')
pl.show()




