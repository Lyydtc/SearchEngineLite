# -*- coding: utf-8 -*-
from collections import defaultdict
import math
import operator
import csv

arc = 1
NUM = 0

def feature_select(list_words):
    # 总词频统计
    doc_frequency = defaultdict(int)
    csv_ana = csv.reader(open('E:/ana.csv', 'r'))
    num = [row[1] for row in csv_ana]
    flag = [row[0] for row in csv_ana]
    print(flag)
    for word_list in list_words:
        for i in flag:
          if num[NUM] == arc:
              if word_list == i :
                 doc_frequency[i] += 1

    # 计算每个词的TF值
    word_tf = {}  # 存储没个词的tf值
    const = 0
    for i in doc_frequency:
        word_tf[i] = doc_frequency[i] / sum(doc_frequency.values())
        const = const + 1

    # 计算每个词的IDF值
    doc_num = len(list_words)
    word_idf = {}  # 存储每个词的idf值
    word_doc = defaultdict(int)  # 存储包含该词的文档数
    for i in doc_frequency:
        for j in list_words:
            if i in j:
                word_doc[i] += 1
    for i in doc_frequency:
        word_idf[i] = math.log(doc_num / (word_doc[i] + 1))

    # 计算每个词的TF*IDF的值
    word_tf_idf = {}
    for i in doc_frequency:
        word_tf_idf[i] = word_tf[i] * word_idf[i]

    # 对字典按值由大到小排序
    dict_feature_select = sorted(word_tf_idf.items(), key=operator.itemgetter(1), reverse=True)
    return dict_feature_select , const


if __name__ == '__main__':
    k = 0
    csv_file = csv.reader(open('E:/number.csv', 'r'))
    dataset = []
    content = []  # 用来存储整个文件的数据，存成一个列表，列表的每一个元素又是一个列表，表示的是文件的某一行
    column = [row[1] for row in csv_file]  # 拿到所有的单词编号
    dataset += column  # 待处理的数据
    data_list = dataset  # 加载数据
    while k < 137:
       features ,a = feature_select(data_list)  # 所有词的TF-IDF值
       i = 0
       while i < a-1 :   # 将不重复单词表写入文件
           f = open("E:/tf_idf.csv", 'a', newline='')
           writer = csv.writer(f)
           writer.writerow([features[i][0], features[i][1]])
           i = i + 1
       arc = arc+1
       NUM = NUM+1
       k = k+1