# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import csv
import time
import trie
def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

#————————注意事项—————————：
#1. column0中存的是网址，它下标从0开始，为了美观存入csv时变成了 i+1
#2.X_ff中存的无重复的单词，同column0，我把他的编号也变成了 下标+1
#读取再大的文章数目时，X_ff可能越界，numb中存的是文章数，但我遍历时设置的200
if __name__ == '__main__':
    from trie import TrieNode
    t= TrieNode()
    csv_file = csv.reader(open('E:/SearchEngineLite/mySpider/news.csv', 'r'))
    # print(csv_file)  # 可以先输出看一下该文件是什么样的类型
    X_ff = [0]*20000
    flag = [0]*10000
    artry = [0]*10000
    content = []  # 用来存储整个文件的数据，存成一个列表，列表的每一个元素又是一个列表，表示的是文件的某一行
    column = [row[2] for row in csv_file]
    column0 = [row[0] for row in csv_file]
    numb = 0
    flag1 = 0
    flag2 = 0
    k = 0
    for i in column:
        numb = numb+1      #记录总计的文章数
    i = 0
    while i < 200:
       column[i] = column[i].replace(',', '')
       column[i] = column[i].replace('.', '')
       column[i] = column[i].replace('"', '')
       column[i] = column[i].replace(';', '')
       column[i] = column[i].replace('?', '')
       column[i] = column[i].replace('!', '')
       column[i] = column[i].replace('_', '')
       column[i] = column[i].replace(')', '')
       column[i] = column[i].replace('(', '')
       flag[i]=column[i].split()      #分割符号串
       j=0
       while j < len(flag[i])-1:       #将i文章中的单词拆开放进artry中
           artry[flag2] = flag[i][j]
           flag2 = flag2+1
           j = j+1
       while k < flag2 :  #遍历artry
           m = 0
           count = 0
           while  m <= flag1:
                if artry[k] == X_ff[m]:  #若已存
                     count = count+1
                m = m+1
           if count == 0 :  #未存
                   X_ff[flag1] = artry[k]
                   flag1 = flag1+1
           k = k+1
       n1 = 0
       while n1 <= flag2:  #遍历
           n2 = 0
           while n2 <= flag1 :
               if X_ff[n2] == flag[i][n1] :
                f = open("E:/ana.csv", 'a', newline='')
                writer = csv.writer(f)
                writer.writerow([n2+1,i+1])   #在i+1之前，i文章的索引已经建立成功
               n2 = n2+1
           n1 = n1+1
       k = 0
       flag2 = 0
       i = i+1
    i = 0
    while i <= flag1:     #将不重复单词表写入文件
        f = open("E:/number.csv", 'a', newline='')
        writer = csv.writer(f)
        MD = X_ff[i]
        writer.writerow([MD,i+1])
        i = i+1
        f.close()
    # while i <= flag1 :
    #     print(X_ff[i])
    #     i = i+1
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
