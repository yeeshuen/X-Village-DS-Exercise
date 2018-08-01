from lib.queue import Queue

q = Queue()

class q:
    ##初始queue
    def __init__(self):
        self.items = []

    #判斷queue是否空
    def isEmpty(self):
        return len(self.items) == []
    
    #進queue
    def enqueue(self, item):
        self.items.insert(0,item)

    #出queue
    def dequeue(self):
        return self.items.pop()

    #queue length
    def size(self):
        return len(self.items)


def hot_potato(namelist, num):
    q = Queue()
    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num):
          q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()

print(hot_potato(["Susan","Brad","Kent","David"], 6))
print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))

#references- https://blog.csdn.net/LLM666Coder/article/details/79809425