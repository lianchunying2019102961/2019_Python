import random

import string



class DataGeneration:

    """Generate random data"""



    STR = [chr(i) for i in range(65, 91)]

    str = [chr(i) for i in range(97, 123)]

    number = [chr(i) for i in range(48, 58)]

    initspecial = string.punctuation



    @staticmethod

    def str_generation():  # �����ַ���

        special = []

        for i in DataGeneration.initspecial:

            special.append(i)

        total = DataGeneration.STR + DataGeneration.str + DataGeneration.number + special

        return ''.join(random.sample(total, random.randint(1, 10)))



    @staticmethod

    def dict_key_generation():  # ���ɼ�ֵ��

        total = DataGeneration.STR + DataGeneration.str

        str = ''.join(random.sample(total, random.randint(1, 10)))

        length = len(str)

        mydict = {str: length}

        return mydict



    @staticmethod

    def data_generation(filename, size):  # �����������,��ʼidΪstart_id������0-100��������������������������ַ����������ֵ��

        f = open(filename, "w")

        for i in range(0, size):

            data = {"_id": i,

                    "random_int": random.randint(0, 100),

                    "random_float": random.uniform(0, 100),

                    "random_string": DataGeneration.str_generation(),

                    "random_dict": DataGeneration.dict_key_generation()}

            s = str(data)

            f.write(s + '\n')