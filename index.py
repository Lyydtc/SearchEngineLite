import csv
import sys


def Pre():
    # 前提 设定内存缓冲区最多可容纳1024个整数
    PAGE_SIZE = 4096  # page = 4KB
    BUF_PAGES = 32
    BUF_SIZE = PAGE_SIZE * BUF_PAGES
    BUF_LEN = int(PAGE_SIZE / 4)  # 归并段长度不得大于1096/4=1024
    return BUF_LEN


def read():
    data = []
    with open(r'G:\dm\sf_kcsj\sy\\temp_index.csv', 'r') as file:# 路径修改
        reader = csv.reader(file)
        for line in reader:
            data.append(line)  # 将csv中内容（临时索引）读入data列表
    return data


def run(length, datalength):
    num = 4
    for r in range(sys.maxsize):
        l = int(datalength / num) + 1
        if l < length - 1:
            break
        num = num * 4
    return l


def trans(data, num_runs, run_length, m_length, m):
    run_1 = [[0 for a in range(run_length)] for b in range(num_runs)]
    run_2 = [[0 for a in range(run_length)] for b in range(num_runs)]
    for i in range(num_runs):
        if i >= m:
            for j in range(m_length - 1):
                run_1[i][j] = int(data[m * run_length + (i - m) * m_length + j][0])
                run_2[i][j] = int(data[m * run_length + (i - m) * m_length + j][1])
            run_1[i][m_length - 1] = MAX
            run_2[i][m_length - 1] = MAX
        else:
            for j in range(run_length - 1):
                run_1[i][j] = int(data[i * run_length + j][0])
                run_2[i][j] = int(data[i * run_length + j][1])
            run_1[i][run_length - 1] = MAX
            run_2[i][run_length - 1] = MAX

    transdata1 = []
    transdata2 = []
    for i in range(num_runs):
        for j in range(run_length):
            transdata1.append(run_1[i][j])
            transdata2.append(run_2[i][j])
    transdata = [transdata1, transdata2]
    # print(transdata)
    return transdata


def sort(transdata, num_runs, run_length, m_length, n):
    temp = [[0 for a in range(run_length)] for b in range(2)]
    sortdata = []
    for i in range(num_runs):
        sortdata1 = []
        sortdata2 = []
        for j in range(run_length):
            temp[0][j] = transdata[0][run_length * i + j]
            temp[1][j] = transdata[1][run_length * i + j]
        if i < n:
            for t in range(run_length - 1):
                for p in range(1, run_length - t):
                    k = run_length - p
                    if temp[0][k] > temp[0][k - 1]:
                        tem1 = temp[0][k]
                        temp[0][k] = temp[0][k - 1]
                        temp[0][k - 1] = tem1
                        tem2 = temp[1][k]
                        temp[1][k] = temp[1][k - 1]
                        temp[1][k - 1] = tem2
            for m in range(run_length):
                transdata[0][run_length * i + m] = temp[0][m]
                transdata[1][run_length * i + m] = temp[1][m]
        else:
            for t in range(m_length - 1):
                for p in range(1, run_length - t):
                    k = run_length - p
                    if temp[0][k] > temp[0][k - 1]:
                        tem1 = temp[0][k]
                        temp[0][k] = temp[0][k - 1]
                        temp[0][k - 1] = tem1
                        tem2 = temp[1][k]
                        temp[1][k] = temp[1][k - 1]
                        temp[1][k - 1] = tem2
            for m in range(run_length):  # 将最后一个子归并段赋给临时数组进行处理
                transdata[0][run_length * i + m] = temp[0][m]
                transdata[1][run_length * i + m] = temp[1][m]
        for k in range(run_length):
            sortdata1.append(transdata[0][run_length * i + k])
            sortdata2.append(transdata[1][run_length * i + k])
        sortdata.append(sortdata1)
        sortdata.append(sortdata2)
    # print(sortdata)
    return sortdata


def adjust(s):
    t = (s + K) // 2  # 取s位的父节点

    # 如果当前节点不是根节点则进入下次循环，否则跳出
    while t > 0:
        # 比较当前节点值与父节点对应的值，如果父节点胜出则记录失败者并将当前节点换成胜利者
        if value[s] > value[ls[t]]:
            l = ls[t]
            ls[t] = s
            s = l
        t = t // 2
    # 记录最终胜利者到ls[0]
    ls[0] = s


def Init():
    value.append(-1)
    for i in range(len(value)):
        ls.append(len(value) - 1)
    for i in range(K):
        adjust(i)


def split(windata, length, num):
    splitdata = []
    for x in range(num):
        temp = []
        tem = []
        for j in range(length):
            temp.append(windata[x * length + j])
        temp.append(MAX)
        for j in range(length + 1):
            tem.append(temp.pop())
        splitdata.append(tem)
    # print(splitdata)
    # print(len(splitdata))
    return splitdata


def check(windata):
    checkdata1 = []
    checkdata2 = []
    start = 0
    now = 0
    end = 0
    c = 0
    judge = 0
    for w in range(len(windata[0])):
        if windata[0][w] == 0:
            now = windata[0][w + 1]
            start = w + 1
            continue
        if windata[0][w] == now:
            judge = 0
            if start == w:
                string = str(windata[1][w])
            else:
                for k in range(start, w):
                    if windata[1][k] == windata[1][w]:
                        judge = 1
                        break
                if judge != 1:
                    string = string + ',' + str(windata[1][w])
        else:
            if w < (len(windata[0]) - 1):
                checkdata1.append(now)
                checkdata2.append(string)
                start = w + 1
                now = windata[0][w + 1]
                c = c + 1
            else:
                checkdata1.append(now)
                checkdata2.append(string)
                c = c + 1
    checkdata = []
    for tc in range(c):
        checkdata.append([checkdata1[tc], checkdata2[tc]])
    print(checkdata)
    return checkdata


MAX = sys.maxsize
Data = read()
Length = Pre()
DataLength = len(Data)
Run_length = run(Length, DataLength)
Num_runs = int(DataLength / Run_length) + 1  # 归并段数=总长/归并路数，取整加一
M = Num_runs - (Num_runs * Run_length - DataLength)
K = 4

Transdata = trans(Data, Num_runs, Run_length, Run_length - 1, M)

Sortdata = sort(Transdata, Num_runs, Run_length, Run_length - 1, M)

Lsdata_t = []
Lsdata_d = []
windata_t = []
windata_d = []

nnum = 0
# first run
for i in range(int(len(Sortdata) / 2)):
    Lsdata_t.append(Sortdata[2 * i])
for i in range(int(len(Sortdata) / 2)):
    Lsdata_d.append(Sortdata[2 * i + 1])
    count = 0
    ls = []
for i in range(int(Num_runs / 4)):
    value = []
    rundata_t = []
    rundata_d = []
    for j in range(4):
        rundata_t.append(Lsdata_t[4 * i + j])
        rundata_d.append(Lsdata_d[4 * i + j])
    for k in range(4):
        value.append(rundata_t[k].pop())
    Init()
    while value[ls[0]] < MAX:
        # print(value,ls[0])
        winner = ls[0]
        windata_t.append(value[winner])
        windata_d.append(rundata_d[winner].pop())
        value[winner] = rundata_t[winner].pop()
        adjust(winner)
ls = []
value = []
Num = 4
for time in range(1, sys.maxsize):
    if Num == Num_runs:
        break
    Num = 4 * Num
N = Num_runs
l = Run_length - 1
for t in range(time):
    N = N / 4
    l = l * 4
    if N != 1:
        Lsdata_t = split(windata_t, l, int(N))
        Lsdata_d = split(windata_d, l, int(N))
        windata_t = []
        windata_d = []
        for i in range(int(N / 4)):
            value = []
            rundata_t = []
            rundata_d = []
            for j in range(4):
                rundata_t.append(Lsdata_t[4 * i + j])
                rundata_d.append(Lsdata_d[4 * i + j])
            for k in range(4):
                value.append(rundata_t[k].pop())
            Init()
            while value[ls[0]] < MAX:
                # print(value,ls[0])
                winner = ls[0]
                windata_t.append(value[winner])
                windata_d.append(rundata_d[winner].pop())
                value[winner] = rundata_t[winner].pop()
                adjust(winner)
    else:
        break

Windata = [windata_t, windata_d]
Checkdata = check(Windata)
# enddata = endsort(Checkdata)
for i in range(len(Checkdata)):
    f = open("G:\dm\sf_kcsj\sy\Elasticsearch.csv", 'a', newline='')   #路径修改
    writer = csv.writer(f)
    writer.writerow(Checkdata[i])
    f.close()
