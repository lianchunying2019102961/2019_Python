import pymongo
import random
client = pymongo.MongoClient('mongodb')
db = myclient.list

from pymongo import MongoClient
db = myclient.test  
my_set = db.test_set
with open('ans.txt', 'r') as f:
    for line in f.readlines():    
        ans.insert({ 'ans':1})

********************************
��
********************************
use tblorders;
 
db.tblorders.insert( {sfbshfi" } );
db.tblorders.insert( { "4089902"} );
db.tblorders.find();
********************************
ɾ
********************************
#ɾ�������������һ��
db.tblorders.update({ "id": 1 }, { $unset: {"naje" : 1} }) ;
********************************
�� 
********************************
#������ocpyang����ΪAtalas 
db.tblorders.update({ name: "ocpyang" }, { $set: {name: "Atalas"} },false,true) ;
 
********************************
��
********************************

#����1
db.tblorders.find();
 
#����2
db.tblorders.find({"kiki"});
 
#����3
db.tblorders.find({"kiki"}).limit(1);
 
#����4
db.tblorders.find({"kiki"}).forEach(printjson);
