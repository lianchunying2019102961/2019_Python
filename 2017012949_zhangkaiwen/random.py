import pymongo
import random
from pymongo import MongoClient

a={'����':['����','����','����','����'],
   '����':['��','��','��','��','¹'],
   '����':['��','Ѽ','��'],
   '����':['����','��','������','��','����']
   }
l=list(a.keys())

"""
��mongodb�д�����һ����Ϊ'firstpy'�����ݿ⣬���м��Ͻ�'dongwu'
"""

client=pymongo.MongoClient('localhost',27017)
dblist=client['firstpy']
dongwu=dblist.dongwu

"""
��������
"""
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
    return 'finish'
if __name__ == '__main__':
    file = open("out.txt", "w")
    for data in generaterandom(100000):
        file.write(str(data)+'\n')
    file.close()

"""
ɾ������
"""

def dele(cata,data):
dongwu.delete_one({cata:data})