# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:52:42 2019

@author: hp
"""
import matplotlib.pyplot as plt
import numpy as np
from pymongo import MongoClient
from data_generate import Generate
from run_mongo import mongo
from visualization import matplot

if __name__ == '__main__':
    mongo.build()
    matplot.picture()#调用前三次作业函数，实验功能

