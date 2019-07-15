import pymongo
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import random
from pymongo import MongoClient

a={'����':['����','����','����','����'],
   '����':['��','��','��','��','¹'],
   '����':['��','Ѽ','��'],
   '����':['����','��','������','��','����']
   }
l=list(a.keys())

client=pymongo.MongoClient('localhost',27017)#�������ݿ�
dblist=client['firstpy']#���ݿ���
dongwu=dblist.dongwu#������

def generaterandom(size):
    while size>0:
        randomint=random.randint(0,100)
        randomfloat=random.random()
        randomchar=random.choice('asdfghjQWERZXC!@#$%^&')
        door=random.choice(l)
        animal=random.choice(a[door])
        temp=(randomint,randomfloat,randomchar,door+'['+animal+']')
        yield temp
        randnum={
            '����':randomint,
            '������':randomfloat,
            '�ַ�':randomchar,
            '��':door,
            "����":animal
        }
        dongwu.insert_one(randnum)
        size=size-1
if __name__ == '__main__':
    file = open("out.txt", "w")
    for data in generaterandom(100000):
        file.write(str(data)+'\n')
    file.close()

data=pd.DataFrame(list(dongwu.find()))
y=data['����']
x=data['������']
fig=plt.figure(figsize=(5,5))
ax=fig.add_subplot(111)
plt.xlabel('X')
plt.ylabel('Y')
ax.scatter(x,y,c='green')
ax.legend=('x1')
ax.grid(True)
plt.show()