import string
import random
from pymongo import MongoClient

#1.���ӱ������ݿ����
#2.���ӱ������ݿ� demo û�лᴴ��
#3.���������Ӽ���
name = MongoClient('localhost'��27017)
db = name.zhougn   #demo���ݿ���
emp = db.zhougn576  #��������
emp.remove(None)

def Random(i):
    cout=0
    while i!=0:
        cout+=1
        num=random.randint(1,10)
        ran_str =  ''.join(random.sample(string.ascii_letters + string.digits,num))
        unif=random.uniform(1,100)
        rand=random.randint(1,1000)
        key=random.choice(string.ascii_letters)
        dict1={key:unif}
        dict2={key:rand}
        dict3={key:ran_str}
        cout1=(str(cout)+':')
        tup1 = (cout1,ran_str,unif,rand,dict1,dict2,dict3)
        yield tup1
        randomNumber = {
            '���':cout,
            '����': rand,
            '������':unif,
            '�ַ�': ran_str,
            '�ֵ�1': dict1,
            '�ֵ�2':dict2,
            '�ֵ�3':dict3
        }
        emp.insert_one(randomNumber)
        i= i - 1
    return 'done'
g = Random(100000)
f = open("db.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()