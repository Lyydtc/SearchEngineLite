import csv
import time


if __name__ == "__main__":
    tic = time.time()
    with open(r".\mySpider\news.csv") as fin1, open(r".\pages.csv", "w", newline='') as fout1:
        news_reader = csv.reader(fin1)
        news_writer = csv.writer(fout1)
        count = 0
        did = 0
        for row in news_reader:
            count += 1
            if count in range(4399, 4524) or count in range(3673, 3815) or count in range(395, 449):
                continue
            did += 1
            news_writer.writerow([did, row[0]])
    with open(r".\mySpider\rmrb.csv", encoding='utf-8') as fin2, open(r".\pages.csv", "a", newline='') as fout2:
        rmrb_reader = csv.reader(fin2)
        rmrb_writer = csv.writer(fout2)
        count = 0
        for row in rmrb_reader:
            count += 1
            if count == 1:
                continue
            did += 1
            rmrb_writer.writerow([did, row[0]])
    toc = time.time()
    print(toc-tic)
