import json
import numpy as np 
from matplotlib import pyplot as plt 
# ��������
file = open('test.txt', 'r') 
js = file.read()
dic = json.loads(js)   
file.close() 
# ��ȡ����
y = []
for i in range(100000):
    y.append(dic[i])
y = np.array(y)
x = np.arange(1,100000)
# �滭
plt.scatter(x,y,c = 'r',marker = 'o')
plt.show()