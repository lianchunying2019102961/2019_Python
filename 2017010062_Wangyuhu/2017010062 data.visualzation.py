# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np



class DataVisualization:

    """Data Visualization"""



    @staticmethod

    def draw_plot(x, y0, y1, target):  # targetΪĿ�����ݿ�Ϊrandom_int����random_float

        fig, ax1 = plt.subplots()

        if target == 'random_int':

            ax1.plot(x, y0, color='red', linestyle='-', marker="*")

            ax1.set_xlabel('id')

            ax1.set_ylabel('random_int')

        elif target == 'random_float':

            ax1.plot(x, y1, color='blue', linestyle='-.', marker="*")

            ax1.set_xlabel('id')

            ax1.set_ylabel('random_float')

        elif target == 'both':

            ax2 = ax1.twinx()

            ax1.plot(x, y0, color='red', linestyle='-', marker="*")

            ax2.plot(x, y1, color='blue', linestyle='-.', marker="*")

            ax1.set_xlabel('id')

            ax1.set_ylabel('random_int')

            ax2.set_ylabel('random_float')

        plt.show()



    @staticmethod

    def draw_bar(x, y0, y1, target, style):  # targetΪĿ�����ݣ���Ϊrandom_int����random_float,styleΪ��ʽ����Ϊvertical����horizontal

        fig, ax1 = plt.subplots()

        if target == 'random_int':

            if style == 'vertical':

                ax1.bar(x, y0, color='red', align='center')

                ax1.set_xlabel('id')

                ax1.set_ylabel('random_int')

            elif style == 'horizontal':

                ax1.barh(x, y0, color='red', align='center')

                ax1.set_ylabel('id')

                ax1.set_xlabel('random_int')

        elif target == 'random_float':

            if style == 'vertical':

                ax1.bar(x, y1, color='blue', align='center')

                ax1.set_xlabel('id')

                ax1.set_ylabel('random_int')

            elif style == 'horizontal':

                ax1.barh(x, y2, color='blue', align='center')

                ax1.set_ylabel('id')

                ax1.set_xlabel('random_float')

        plt.show()



    @staticmethod

    def draw_pie(data, size):  # ��random_int��random_floatһ��������仮�ֲ�ͳ��

        fig, ax1 = plt.subplots()

        a, b, c, d = 0, 0, 0, 0

        for i in range(size):

            if (data[i]['random_int'] >= 0) & (data[i]['random_int'] <= 25):

                a = a + 1

            if (data[i]['random_int'] > 25) & (data[i]['random_int'] <= 50):

                b = b + 1

            if (data[i]['random_int'] > 50) & (data[i]['random_int'] <= 75):

                c = c + 1

            if (data[i]['random_int'] > 75) & (data[i]['random_int'] <= 100):

                d = d + 1

            if (data[i]['random_float'] >= 0) & (data[i]['random_float'] <= 25):

                a = a + 1

            if (data[i]['random_float'] > 25) & (data[i]['random_float'] <= 50):

                b = b + 1

            if (data[i]['random_float'] > 50) & (data[i]['random_float'] <= 75):

                c = c + 1

            if (data[i]['random_float'] > 75) & (data[i]['random_float'] <= 100):

                d = d + 1

        labels = '[0-25]', '(25-50]', '(50-75]', '(75-100]'

        sizes = [a / 100, b / 100, c / 100, d / 100]

        ax1.pie(sizes, labels=labels, autopct='%1.2f%%', shadow=True)

        plt.show()



    @staticmethod

    def draw_hist(y0, y1, target):  # targetΪĿ�����ݿ�Ϊrandom_int����random_float

        num_bins = 50

        fig, ax1 = plt.subplots()

        if target == 'random_int':

            ax1.hist(y0, num_bins, density=True, facecolor='blue', alpha=0.5)

            ax1.set_ylabel('random_int')

        elif target == 'random_float':

            ax1.hist(y1, num_bins, density=True, facecolor='blue', alpha=0.5)

            ax1.set_ylabel('random_float')

        plt.show()



    @staticmethod

    def draw_scatter(x, y0, y1, target):  # targetΪĿ�����ݿ�Ϊrandom_int����random_float

        fig, ax1 = plt.subplots()

        area = (30 * np.random.rand(50)) ** 2

        colors = np.random.rand(50)

        if target == 'random_int':

            plt.scatter(x, y0, s=area, c=colors, alpha=0.5)

            ax1.set_ylabel('random_int')

        elif target == 'random_float':

            plt.scatter(x, y1, s=area, c=colors, alpha=0.5)

            ax1.set_ylabel('random_float')

plt.show()