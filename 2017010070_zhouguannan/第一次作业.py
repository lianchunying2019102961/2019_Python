import random
import string

cout=0
for i in range(100000):
    cout+=1
    print(cout,".",end='  ')#���ݱ��
    print(random.uniform(1,100),end='  ')#������ɷ�Χ��1-100��С��
    RandomStr =  ''.join(random.sample(string.ascii_letters + string.digits, 10))#����Ϊ10���ַ���
    print(RandomStr,end='  ')
    print(random.randint(1,1000),end='  ')
    x=random.randint(1,10)
    dict1={random.choice(string.ascii_letters):random.sample(string.ascii_letters+string.digits,x)}
    print(dict1)