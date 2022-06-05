import csv
import time


if __name__ == "__main__":
    # 开始计时
    tic = time.time()
    # 对news.csv进行操作
    with open(r".\files\news.csv") as fin1, open(r".\files\pages.csv", "w", newline='') as fout1:
        news_reader = csv.reader(fin1)
        news_writer = csv.writer(fout1)
        count = 0  # 第几条数据
        did = 0  # 网页编号
        for row in news_reader:
            count += 1
            if count in range(4399, 4524) or count in range(3673, 3815) or count in range(395, 449):
                continue
            did += 1
            news_writer.writerow([did, row[0]])
    # 对rmrb.csv进行操作，要用utf-8编码打开，a代表追加
    with open(r".\files\rmrb.csv", encoding='utf-8') as fin2, open(r".\files\pages.csv", "a", newline='') as fout2:
        rmrb_reader = csv.reader(fin2)
        rmrb_writer = csv.writer(fout2)
        count = 0
        for row in rmrb_reader:
            count += 1
            if count == 1:
                continue
            did += 1
            rmrb_writer.writerow([did, row[0]])
    # 计时结束
    toc = time.time()
    # 打印耗时
    print("times:", toc-tic)
