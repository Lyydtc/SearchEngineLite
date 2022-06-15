import csv
from trie import TrieNode
import re
from cn_segment import bi_segment

frequency_list3 = [0] * 100000  # 存放初始每个页面出现次数（初始均为0）
pagenum_frequency_list5 = []  # 存放页码以及对应的出现次数
temp_list = []  # 归并排序中存放临时数据


# 将输入字符串分为词列表
def seg_str(sen: str):
    a = re.findall(u"[\u4e00-\u9fa5]+", sen)
    print(f"cn list = {a}")
    b = re.findall('[a-zA-Z]+', sen)
    print(f"en list = {b}")
    c = re.findall('[0-9]+', sen)
    print(f"d list = {c}")
    return word_list


# 输出单词列表的单词编号列表
def find_tid(word_list):
    tid_list = []
    t = TrieNode()
    with open(r'./files/term_id.csv', encoding='utf8') as f:
        tid_reader = csv.reader(f)
        for row in tid_reader:
            t.insert(row[1], row[0])
        for word in word_list:
            result = t.search(word)
            if result[0]:
                tid_list.append(result[1])
    return tid_list


def find_didlist(tid_list):
    didlist_list = []
    with open('C:\\Users\\26292\\Desktop\\inverted_index.csv') as f1:
        reader = csv.reader(f1)
        l = list(reader)
        for tid in tid_list:
            m = 0
            while m < len(l):
                if tid == l[m][0]:
                    didlist_list.extend(str(l[m][1:][0]).split(','))
                    break
                m += 1
    return didlist_list


def cal_didlist(didlist_list):
    m = 0
    num = 0
    final_didlist = []
    while m < len(didlist_list):
        num = int(didlist_list[m]) - 1
        frequency_list3[num] = frequency_list3[num] + int(didlist_list[m][1])
        m += 1
    m = 0
    while m < 10000:  # 总共网页个数，我设置了个10000
        pagenum_frequency_list5.append([str(m + 1), str(frequency_list3[m])])
        m += 1
    erfen(pagenum_frequency_list5, temp_list, 0, len(pagenum_frequency_list5) - 1)
    for row in pagenum_frequency_list5:
        if (row[1] != '0'):
            final_didlist.append(row[0])
    return final_didlist


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


def show_pages(did_list):
    with open(r'./files/pages.csv') as f:
        page_reader = csv.reader(f)
        ll = list(page_reader)
        judge = 0
        for did in did_list:
            n = 0
            while n < len(ll):
                if did == str(ll[n][0]):
                    judge = 1
                    print(ll[n][2] + '\n' + ll[n][1] + '\n')
                    break
                n += 1
        if (judge == 1):
            print('已为您找到如上搜索结果')
        else:
            print('没有找到您想搜索的数据')
    return


if __name__ == '__main__':
    sen = input('请输入关键词：\n')

    word_list = seg_str(sen)  # 得到词语列表
    tid_list = find_tid(word_list)  # 得到单词编号
    didlist_list = find_didlist(tid_list)  # 得到对应网页编号
    did_list = cal_didlist(didlist_list)  # 得到最终网页编号
    show_pages(did_list)  # 呈现搜索结果
# package adopt stabilize
