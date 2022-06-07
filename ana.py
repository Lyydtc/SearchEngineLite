import csv
import time
from trie import TrieNode
from cn_segment import bi_segment


# ————————注意事项—————————：
# 1. column0中存的是网址，它下标从0开始，为了美观存入csv时变成了 i+1
# 2.X_ff中存的无重复的单词，同column0，我把他的编号也变成了 下标+1
# 读取再大的文章数目时，X_ff可能越界，numb中存的是文章数，但我遍历时设置的200
# if __name__ == '__main__':
#     t = TrieNode()
#     csv_file = csv.reader(open(r'./files/news.csv', 'r'))
#     # print(csv_file)  # 可以先输出看一下该文件是什么样的类型
#     X_ff = [0]*20000  # 不同单词
#     flag = [0]*10000  #
#     artry = [0]*10000  #
#     content = []  # 用来存储整个文件的数据，存成一个列表，列表的每一个元素又是一个列表，表示的是文件的某一行
#     column = [row[2] for row in csv_file]
#     column0 = [row[0] for row in csv_file]
#     numb = 0
#     flag1 = 0
#     flag2 = 0
#     k = 0
#     for i in column:
#         numb = numb+1      # 记录总计的文章数
#     i = 0
#     while i < 200:
#        column[i] = column[i].replace(',', '')
#        column[i] = column[i].replace('.', '')
#        column[i] = column[i].replace('"', '')
#        column[i] = column[i].replace(';', '')
#        column[i] = column[i].replace('?', '')
#        column[i] = column[i].replace('!', '')
#        column[i] = column[i].replace('_', '')
#        column[i] = column[i].replace(')', '')
#        column[i] = column[i].replace('(', '')
#        flag[i] = column[i].split()      # 分割符号串
#        j = 0
#        while j < len(flag[i])-1:       # 将i文章中的单词拆开放进artry中
#            artry[flag2] = flag[i][j]
#            flag2 = flag2+1
#            j = j+1
#        while k < flag2:  #遍历artry
#            m = 0
#            count = 0
#            while  m <= flag1:
#                 if artry[k] == X_ff[m]:  #若已存
#                      count = count+1
#                 m = m+1
#            if count == 0 :  #未存
#                    X_ff[flag1] = artry[k]
#                    flag1 = flag1+1
#            k = k+1
#        n1 = 0
#        while n1 <= flag2:  #遍历
#            n2 = 0
#            while n2 <= flag1 :
#                if X_ff[n2] == flag[i][n1] :
#                 f = open("E:/ana.csv", 'a', newline='')
#                 writer = csv.writer(f)
#                 writer.writerow([n2+1,i+1])   #在i+1之前，i文章的索引已经建立成功
#                n2 = n2+1
#            n1 = n1+1
#        k = 0
#        flag2 = 0
#        i = i+1
#     i = 0
#     while i <= flag1:     #将不重复单词表写入文件
#         f = open("E:/number.csv", 'a', newline='')
#         writer = csv.writer(f)
#         MD = X_ff[i]
#         writer.writerow([MD,i+1])
#         i = i+1
#         f.close()
    # while i <= flag1 :
    #     print(X_ff[i])
    #     i = i+1
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助


signs = [' ', '，', '。', '！', '？', '“', '”', '《', '》', '（', '）', '·', '、', '：', '——', '；', '—', '……',
         '.', '>', ',', '(', ')', '<', '>', ';', ':', '.', '?', '!', '"']


# 清洗单词列表，使列表元素为纯英语单词
def clean_list(wordlist: list):
    clean_word_list = []
    for word in wordlist:
        clean_word = ''
        for char in word:
            if (char > 'z' or char < 'a') and (char > 'Z' or char < 'A'):
                continue
            clean_word += char
        if clean_word != '':
            clean_word_list.append(clean_word)
    return clean_word_list


tic = time.time()  # 计时开始

term_id = 0  # 单词编号
num = 0  # 网页编号

# 分析news文件
with open(r'./files/news.csv', 'r') as fin1, \
        open(r'./files/temp_index.csv', 'w', newline='') as fout1, \
        open(r'./files/term_id.csv', 'w', newline='') as fout2:
    news_reader = csv.reader(fin1)
    index_writer = csv.writer(fout1)
    id_writer = csv.writer(fout2)

    count = 0  # 当前是第count条数据，用于已知位置的排除非法数据
    t = TrieNode()

    for row in news_reader:
        count += 1
        if count in range(4399, 4524) or count in range(3673, 3815) or count in range(395, 449):
            continue
        num += 1
        row[2] += row[1]  # 把文本都放入列表row[2]
        row[2] = clean_list(row[2].split()) # 清理文本，生成单词列表

        # 遍历单词列表，写入单词编号文件和临时索引文件
        for word in row[2]:
            if t.search(word):
                continue
            else:
                t.insert(word)
                term_id += 1
                id_writer.writerow([term_id, word])
                index_writer.writerow([term_id, num])
                print(term_id, word)

en_toc = time.time()  # 计时结束
print("分析news.csv耗时：", en_toc-tic)

# 分析rmrb文件
with open(r'./files/rmrb.csv', 'r', encoding='utf-8') as fin2, \
        open(r'./files/temp_index.csv', 'a', newline='') as fout1, \
        open(r'./files/term_id.csv', 'a', newline='', encoding='utf8') as fout2:
    rmrb_reader = csv.reader(fin2)
    index_writer = csv.writer(fout1)
    id_writer = csv.writer(fout2)

    t = TrieNode()
    count = 0

    for row in rmrb_reader:
        num += 1
        count += 1
        if count == 1:
            continue
        row[2] += row[1]  # 把文本都放入列表row[2]
        row[2] = bi_segment(row[2])  # 清理文本，生成单词列表

        # 遍历单词列表，写入单词编号文件和临时索引文件
        for word in row[2]:
            if t.search(word):
                continue
            else:
                t.insert(word)
                term_id += 1
                id_writer.writerow([term_id, word])
                index_writer.writerow([term_id, num])
                print(term_id, word)

cn_toc = time.time()  # 计时结束
print("分析rmrb.csv耗时：", cn_toc-tic)
