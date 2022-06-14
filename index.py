import csv
import sys


def Pre():
    # 前提 设定内存缓冲区最多可容纳1024个整数
    PAGE_SIZE = 4096  # page = 4KB
    BUF_PAGES = 32
    BUF_SIZE = PAGE_SIZE * BUF_PAGES
    BUF_LEN = int(PAGE_SIZE / 4)  # 归并段长度不得大于4096/4=1024
    return BUF_LEN


def read():
    read_data = []
    data = []
    with open(r'G:\dm\sf_kcsj\sy\\temp_index.csv', 'r') as file:
        reader = csv.reader(file)
        j = 0
        for row in reader:
            j = j + 1
            read_data.append(row)  # 将csv中内容（临时索引）读入data列表
            if j == 1024:
                temp = quick_sort(read_data)
                data.append(temp)
                j = 0
                read_data = []
    if j != 0:
        temp = quick_sort(read_data)
        data.append(temp)
    # print(data[1919])
    # print(len(data))
    # print(len(data[1953]))
    return data


def quick_sort(arr):
    if len(arr) < 2:
        # 基线条件：为空或只包含一个元素的数组是“有序”的
        return arr
    else:
        # 递归条件
        pivot = int(arr[0][0])
        # 由所有小于基准值的元素组成的子数组
        less = [i for i in arr[1:] if int(i[0]) <= pivot]
        # 由所有大于基准值的元素组成的子数组
        greater = [i for i in arr[1:] if int(i[0]) > pivot]
        return quick_sort(less) + [arr[0]] + quick_sort(greater)


def adjust(s, value, ls):
    m = (s + K) // 2  # 取s位的父节点
    # 如果当前节点不是根节点则进入下次循环，否则跳出
    while m > 0:
        # 比较当前节点值与父节点对应的值，如果父节点胜出则记录失败者并将当前节点换成胜利者
        if value[s] > value[ls[m]]:
            n = ls[m]
            ls[m] = s
            s = n
        m = m // 2
    # 记录最终胜利者到ls[0]
    ls[0] = s
    return ls


def Init(value, ls):
    value.append(-1)
    for i in range(len(value)):
        ls.append(len(value) - 1)
    for i in range(K):
        ls = adjust(i, value, ls)
    return ls


def repeat(k_data):
    value = []
    ls = []
    num = [[0] for i in range(K)]
    windata = []
    for lenk in range(len(k_data)):
        value.append(int(k_data[lenk][0][0]))
    ls = Init(value, ls)
    while value[ls[0]] < MAX:
        winner = ls[0]
        windata.append(k_data[winner][num[winner][0]])
        if num[winner][0] == (len(k_data[winner]) - 1):
            value[winner] = MAX
        else:
            num[winner][0] = num[winner][0] + 1
            value[winner] = int(k_data[winner][num[winner][0]][0])
        adjust(winner, value, ls)
    # print(len(windata))
    return windata


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)
    return(arr)


def heapSort(arr):
    n = len(arr)
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)
    return arr


def manage2(com):
    m2 = heapSort(com)
    m1 = [m2[0]]
    j = 0
    for i in range(1, len(m2)):
        if m2[i] != m2[i - 1]:
            m1.append(m2[i])
    return m1


def manage1(m_data):
    r1 = []
    r2 = []
    r = []
    compare = []
    for i in range(1, len(m_data)):
        compare.append(int(m_data[i-1][1]))
        if m_data[i][0] != m_data[i - 1][0]:
            if len(compare) == 1:
                r2.append(compare)
            else:
                r2.append(manage2(compare))
            r2 = r2[0]
            r.append([int(m_data[i-1][0]), r2])
            r2 = []
            r1 = []
            compare = []
    return r


MAX = sys.maxsize
Data = read()
Length = len(Data)
K = 128
k = 0
Run = [Data]
run = []
count = 1
for t in range(MAX):
    temp = []
    Run.append(temp)
    temp = Run[t]
    if Length == 1:
        sort = Run[t][0]
        break
    else:
        for L in range(len(temp)):
            run.append(temp[L])
            k = k + 1
            if k == K:
                k = 0
                # print(run)
                Run[t + 1].append(repeat(run))
                run = []
        if k != 0:
            K = k
            k = 0
            Run[t + 1].append(repeat(run))
            run = []
    K = 128
    Length = int(Length / K) + 1
print(1)
print(len(sort))
Result = manage1(sort)
for i in range(len(Result)):
    f = open("G:\dm\sf_kcsj\sy\Elasticsearch.csv", 'a', newline='')
    writer = csv.writer(f)
    writer.writerow(Result[i])
    f.close()