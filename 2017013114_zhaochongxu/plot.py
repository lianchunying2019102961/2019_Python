import pymongo
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from pymongo import MongoClient
import random

"""
�������ݿ⣬��������
"""
client=pymongo.MongoClient('localhost',27017)
dblist=client['firstpy']
dongwu=dblist.dongwu
data=pd.DataFrame(list(dongwu.find()))

"""
ͳ�������͸�����
"""
y=data['����']
x=data['������']
fig=plt.figure(figsize=(5,5))
ax=fig.add_subplot(111)
plt.xlabel('X')
plt.ylabel('Y')
ax.scatter(x,y,c='green')
ax.legend=('X1')
ax.grid(True)
plt.show()