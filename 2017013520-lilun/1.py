import random
import json
# �ֵ�
dic = {}
# �������
for i in range(100000):
    dic[i]=random.randint(0,9)
# ����
js = json.dumps(dic)   
file = open('test.txt', 'w')  
file.write(js)  
file.close()