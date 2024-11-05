from multiprocessing import Process
from time import time


def read_info(name):
    all_data = []

    with open(name) as f:
        for line in f:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# start = time()
# for file in filenames:
#     read_info(file)
# end = time()
# print(round(end - start, 2))

# Многопроцессный вывод
if __name__ == '__main__':
    start = time()
    for file in filenames:
        p = Process(target=read_info, args=(file,))
        p.start()
    end = time()
    print(round(end - start, 2))
