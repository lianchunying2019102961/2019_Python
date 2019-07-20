import pymongo

import pandas as pd

import numpy as np  

import matplotlib.pyplot as plt 



# �������ݿ�

client = pymongo.MongoClient('localhost', 27017)

db = client['RandomNumber']

table = db['myrandom']



# ��ȡ����

data = pd.DataFrame(list(table.find()))



# ѡ����Ҫ��ʾ���ֶ�

y = data['int']

z = data['float']



fig = plt.figure()  

ax1 = fig.add_subplot(111)

ax1.set_title('Scatter int') 

ax1.scatter(z,y,c = 'b',marker = 'o')



plt.show()