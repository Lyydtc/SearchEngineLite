#coding=utf-8
import csv
import re
from trie import TrieNode


def forward_segment(text, trie):
    word_list = []
    sen_list = re.split('[，。、：；“”？！—…（）《》*0-9a-z]', text)
    for sen in sen_list:
        i = 0
        while i < len(sen):
            longest_word = sen[i]                       # 当前扫描位置的单字
            for j in range(i + 1, len(sen) + 1):        # 所有可能的结尾
                word = sen[i:j]                         # 从当前位置到结尾的连续字符串
                if trie.search(word)[0]:                # 在词典中
                    if len(word) > len(longest_word):   # 并且更长
                        longest_word = word             # 则更优先输出
            word_list.append(longest_word)              # 输出最长词
            i += len(longest_word)                      # 正向扫描
    return word_list


def backward_segment(text, trie):
    text_word_list = []
    sen_list = re.split('[，。、：；“”？！—…（）《》*0-9a-z]', text)
    for sen in sen_list:
        i = len(sen) - 1
        sen_word_list = []
        while i >= 0:                                   # 扫描位置作为终点
            longest_word = sen[i]                       # 扫描位置的单字
            for j in range(0, i):                       # 遍历[0, i]区间作为待查询词语的起点
                word = sen[j: i + 1]                    # 取出[j, i]区间作为待查询单词
                if trie.search(word)[0]:
                    if len(word) > len(longest_word):   # 越长优先级越高
                        longest_word = word
                        break
            sen_word_list.insert(0, longest_word)       # 逆向扫描，所以越先查出的单词在位置上越靠后
            i -= len(longest_word)
        text_word_list += sen_word_list
    return text_word_list


def count_single_char(word_list: list):  # 统计单字成词的个数
    return sum(1 for word in word_list if len(word) == 1)


def bi_segment(text, t: TrieNode):
    f = forward_segment(text, t)
    b = backward_segment(text, t)
    if len(f) < len(b):                                  # 词数更少优先级更高
        return f
    elif len(f) > len(b):
        return b
    else:
        if count_single_char(f) < count_single_char(b):  # 单字更少优先级更高
            return f
        else:
            return b                                     # 都相等时逆向匹配优先级更高


if __name__ == '__main__':
    t = TrieNode()
    with open(r".\files\dict.csv", encoding='utf-8') as cn_dict_csv:
        cn_dict = csv.reader(cn_dict_csv)
        for word in cn_dict:
            t.insert(word[0])
    print(bi_segment('中国人民解放军', t))
