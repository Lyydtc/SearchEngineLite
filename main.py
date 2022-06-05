s = input('请输入想要搜查的东西')
thislist = s.split(" ")
letterlist = []
letternumlist = []
Inverted_index_list = []
webpagelist = []
list3 = [0] * 1000
list4 = []
list5 = []
i = 1
while i <= 1000:
    list4.append(str(i))
    i += 1
with open('C:\\Users\\26292\\Desktop\\新建 Microsoft Excel 工作表.csv', encoding='utf-8-sig') as df:
    reader = df.readline()
    while reader:
        l = reader.replace('\n', '').split(',')
        letterlist.append(l)
        reader = df.readline()
# 顺序查找单词编号
for a in thislist:
    # judgenum = 0
    for aa in letterlist:
        if (a == aa[0]):
            letternumlist.extend(aa[1:])
        #     break
        # elif (judgenum == len(letterlist)-1 ):
        #     print("没有查找的你想搜索的文字" )
        #     print(a)
        # judgenum += 1
print("已为您找到最相关的网页网址如下")
# 读取倒排索引文件
with open('C:\\Users\\26292\\Desktop\\123工作表.csv', encoding='utf-8-sig') as df1:
    reader = df1.readline()
    while reader:
        l = reader.replace('\n', '').split(',')
        Inverted_index_list.append(l)
        reader = df1.readline()


# 根据单词编号在倒排索引文件里找（二分查找）
def erfen_search(data_list, val):
    low = 0  # 最小数下标
    high = len(data_list) - 1  # 最大数下标
    while low <= high:
        mid = (low + high) // 2  # 中间数下标
        if data_list[mid][0] == val:  # 如果中间数下标等于val, 返回
            return mid
        elif int(data_list[mid][0]) > int(val):  # 如果val在中间数左边, 移动high下标
            high = mid - 1
        else:  # 如果val在中间数右边, 移动low下标
            low = mid + 1
    return -1


for aaa in letternumlist:
    if (erfen_search(Inverted_index_list, aaa) != -1):
        i = 1
        j = erfen_search(Inverted_index_list, aaa)
        while (i < len(Inverted_index_list[j])):
            num = int(Inverted_index_list[j][i]) - 1
            i += 1
            list3[num] = list3[num] + 1

m = 0
while m < 1000:
    list5.append([str(list3[m]), list4[m]])
    m += 1

#
with open('C:\\Users\\26292\\Desktop\\wangzhil 工作表.csv', encoding='utf-8-sig') as df2:
    reader = df2.readline()
    while reader:
        l = reader.replace('\n', '').split(',')
        webpagelist.append(l)
        reader = df2.readline()
for aaaa in list5:
    for aaaaa in webpagelist:
        if (aaaa[0] != '0' and aaaa[1] == aaaaa[0]):
            print(aaaaa[1])
