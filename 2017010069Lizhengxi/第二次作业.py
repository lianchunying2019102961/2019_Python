import string
import random
from pymongo import MongoClient

#1.���ӱ������ݿ����
name = MongoClient('localhost')
#2.���ӱ������ݿ� demo û�лᴴ��
db = name.random_number   #demo���ݿ���
#3.���������Ӽ���
emp = db.myrandom  #��������
emp.remove(None)

def Random(k):
    c=0
    while k!=0:
        c+=1
        wuli=random.randint(1,10)
        ran_str =  ''.join(random.sample(string.ascii_letters + string.digits,wuli))
        leo=random.uniform(1,10)
        m=random.randint(1,100000)
        n=random.choice(string.ascii_letters)
        dicta={n:leo}
        dictb={n:m}
        dictc={n:ran_str}
        c1=(str(c)+':')
        tup1 = (c1,ran_str,leo,m,dicta,dictb,dictc)
        yield tup1
        randomNumber = {
            '���':c,
            '����': m,
            '������':leo,
            '�ַ�': ran_str,
            '�ֵ�1': dicta,
            '�ֵ�2':dictb,
            '�ֵ�3':dictc
        }
        emp.insert_one(randomNumber)
        k= k - 1
    return 'done'
g = Random(100000)
f = open("out.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()

#f1=open("���ݿ�.txt","w")
#for k in emp.find():
 #   print(k,file=f1)
#f1.close()