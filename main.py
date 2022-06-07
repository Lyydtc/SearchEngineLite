s = input('请输入想要搜查的东西')
thislist = s.split(" ")    #存放想要搜索的字符串列表
letterlist = []            #存放爬取的单词列表
letternumlist = []         #存放爬取的单词对应的单词编号列表
Inverted_index_list = []   #存放倒排索引数据列表
webpagelist = []
orderlist = []
list3 = [0] * 10000
list4 = []
list5 = []
temp = []
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
    for aa in letterlist:
        if (a == aa[0]):
            letternumlist.extend(aa[1:])
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
    list5.append([list4[m], str(list3[m])])
    m += 1

def merge(src, temp_list, low, high):
    i = low
    mid = (low + high) // 2
    j = mid + 1

    while (i <= mid) and (j <= high):
        if (src[i][1] < src[j][1]):
            temp_list.append(src[i])
            i += 1
        else:
            temp_list.append(src[j])
            j += 1
    while i <= mid:
        temp_list.append(src[i])
        i += 1
    while j <= high:
        temp_list.append(src[j])
        j += 1

    t = 0
    while low <= high:
        src[low] = temp_list[t]
        low += 1
        t += 1

    temp_list.clear()


def erfen(src, temp_list, low, high):
    if low < high:
        mid = (high + low) // 2
        erfen(src, temp_list, low, mid)  # 递归划分左半区
        # print(['left', low, mid, high])  # 递归划分左半区
        erfen(src, temp_list, mid + 1, high)  # 递归划分右半区
        # print(['right', low, mid + 1, high])  # 递归划分右半区
        # print([low, mid, high])  # 递归划分右半区
        merge(src, temp_list, low, high)  # 最后进行归并


erfen(list5, temp, 0, len(list5) - 1)

with open('C:\\Users\\26292\\Documents\\GitHub\\SearchEngineLite\\files\\pages.csv', encoding='utf-8-sig') as df2:
    reader = df2.readline()
    while reader:
        l = reader.replace('\n', '').split(',')
        webpagelist.append(l)
        reader = df2.readline()
for aaaa in list5:
    for aaaaa in webpagelist:
        if (aaaa[1] != '0' and aaaa[0] == aaaaa[0]):
            print(aaaaa[1])
