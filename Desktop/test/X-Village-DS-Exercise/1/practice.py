#import heapq

#--------------------------------
#https://www.youtube.com/watch?v=GnKHVXv_rlQ 
#push (insert) 换位置
#peek (get max/min) return value to the heap
#pop (remove max/min) remove 

#public functions : push,peek,pop
#private functions : _swap, _floatup, _bubbledown

#---------------------------------------
#class MinHeap:
   # def __init__(self, key, data=())
   #     self.key = key
   #     self.heap = [(self.key(d), d) for d in data]
  #      heapq.heapify(self.heap)
         
    # build a new heap from a list of keys
    #def build_heap(self, keys):
    #    heap.build_heap(self.keys)
    
    # add a new item to the heap
   # def insert(self, item):
    #    heap.insert = []

    #return the item with the minimum key value, removing the item from the heap
  #  def del_min(self):
    #    return self.items()
    
    # print the minimum heap on the screen
    #def display(self):
    #    heap.display 

       

#heap = MinHeap()

#heap.build_heap([9, 5, 6, 2, 3])
#heap.display()

#heap.insert(1)
#heap.insert(7)
#heap.display()

#print(heap.del_min())
#print(heap.del_min())
#heap.display()

#references = https://www.tutorialspoint.com/python/python_heaps.html

import heapq

H = [9, 5, 6, 2, 3]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)


# Add element
heapq.heappush(H,1)
heapq.heappush(H,7)
print(H)

# if Replace an element
#heapq.heapreplace(H,6)
#print(H)