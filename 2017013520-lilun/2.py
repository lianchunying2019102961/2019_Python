import json
import pymongo
# ����MongoDB
client = pymongo.MongoClient(host='localhost', port=27017)
# ָ�����ݿ�
db = client.test
# ָ������
collection = db.randoms
# ��������
file = open('test.txt', 'r') 
js = file.read()
dic = json.loads(js)   
file.close() 
# ��������
result = collection.insert(dic)
# ��ѯ
result2 = collection.find_one({1: 1})
# ��
condition3 = {1: 1}
randoms3 = collection.find_one(condition3)
randoms3[1] = 25
result = collection.update(condition3, randoms3)
print(result)
# ɾ��
result = collection.remove({1: 1})
print(result)