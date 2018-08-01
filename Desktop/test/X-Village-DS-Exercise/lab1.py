#http://nbviewer.jupyter.org/github/x-village/OS_Lab/blob/master/Lab1.ipynb
import numpy as np

def main():
    # Generate random matrix and result matrix
    matA = np.random.randint(10, size = (100, 100))
    matB = np.random.randint(10, size = (100, 100))
    result = np.zeros((matA.shape[0], matB.shape[1]))
    
    for row in range(0, matA.shape[0]):
        result[row] = np.matmul(matA[row], matB)

    # Compare with numpy's multiplication result
    print('Answer is correct:', np.all(np.matmul(matA, matB) == result))
    
if __name__ == "__main__":
    main()

import multiprocessing
import random

def thread_func(process_no, result_queue):
    result_queue.put('Process ' + str(process_no) + ': ' + str(random.randint(0, 10)))

def main():
    # Generate queue for communication
    result_queue = multiprocessing.Manager().Queue()

    processes = 10
    jobs = []

    for i in range(processes):
        process = multiprocessing.Process(target = thread_func, args = (i, result_queue))
        jobs.append(process)

    for process in jobs:
        process.start()

    for process in jobs:
        process.join()

    while not result_queue.empty():
        result = result_queue.get()
        print(result)

if __name__ == "__main__":
    main()

#time
import time

def main():
    start_time = time.time()
    
    a = 0
    for i in range(1000000):
        a = a + 3

    end_time = time.time()
    print('Time elapsed:\t', end_time - start_time)

if __name__ == "__main__":
    main()




#Q1 - Lab1-矩陣平行運算
#Q2 - 分別利用multi-thread和multi-process進行矩陣平行運算
#Q3 - 需要和numpy計算的結果做比對，確保答案正確
#Q4 - 需要計時，並和原本未使用thread或process加速的狀況做效能比較


#Q5 - 隨機產生 10x10 / 100x100 / 1000x1000 的矩陣進行測試，比對不同計算量下的效能提昇
import numpy as np
a=np.random.random((10,10))

print(a)