#100000����̫��
#�˴���ͼ����
# �������ģ��
import pymongo
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt 

x = np.arange(1,100001)
# �������ݿ�
client = pymongo.MongoClient('localhost', 27017)
db = client['random_number']
table = db['myrandom']

# ��ȡ����
data = pd.DataFrame(list(table.find()))
y = data['����']
z = data['������']


fig = plt.figure()  
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.set_title('Scatter int') 
ax2.set_title('Scatter folat')
ax1.scatter(x,y,c = 'g',marker = 'o')
ax2.scatter(x,z,c = 'b',marker = 'x')
plt.show()
)