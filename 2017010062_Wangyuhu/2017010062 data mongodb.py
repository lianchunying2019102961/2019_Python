# -*- coding: utf-8 -*-

class DataStorage:

    """Store the data to mongodb"""



    @staticmethod

    def random_data_storage(mysites, filename):  # �洢size���������

        with open(filename) as file_object:

            for line in file_object:

                mysites.insert_one(eval(line))