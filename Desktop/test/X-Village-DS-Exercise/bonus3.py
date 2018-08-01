#insert sort
#bubble sort
#merge sort
#quick sort
#heap sort

some_list = [
    65, 81, 65, 19, 6, 28, 86, 40, 72, 27,
    76, 46, 22, 98, 49, 57, 52, 46, 47, 14,
    29, 15, 59, 74, 61, 47, 20, 33, 89, 99,
    65, 82, 84, 63, 93, 1, 42, 13, 54, 58,
    84, 17, 5, 18, 14, 14, 19, 42, 60, 77,
    17, 29, 2, 42, 42, 31, 47, 67, 15, 16,
    71, 56, 98, 46, 18, 20, 14, 36, 42, 23,
    87, 7, 5, 5, 52, 78, 76, 91, 92, 88, 38,
    66, 13, 18, 68, 96, 23, 51, 77, 93, 35,
    18, 9, 64, 51, 76, 76, 96, 5, 18
    ]

#insertsort
def insertionSort(some_list):
   for index in range(1,len(some_list)):

     currentvalue = some_list[index]
     position = index

     while position>0 and some_list[position-1]>currentvalue:
         some_list[position]=some_list[position-1]
         position = position-1

     some_list[position]=currentvalue

insertionSort(some_list)
print(some_list)
print('='*30)

#bubblesort
#http://interactivepython.org/courselib/static/pythonds/SortSearch/TheBubbleSort.html

def bubbleSort(some_list):
    for passnum in range(len(some_list)-1,0,-1):
        for i in range(passnum):
            if some_list[i]>some_list[i+1]:
                temp = some_list[i]
                some_list[i] = some_list[i+1]
                some_list[i+1] = temp

bubbleSort(some_list)
print(some_list)

print('='*30)
#merge sort

def mergeSort(some_list):
    print("Splitting ",some_list)
    if len(some_list)>1:
        mid = len(some_list)//2
        lefthalf = some_list[:mid]
        righthalf = some_list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                some_list[k]=lefthalf[i]
                i=i+1
            else:
                some_list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            some_list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            some_list[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",some_list)

mergeSort(some_list)
print(some_list)
print('='*30)

#quicksort 
def quickSort(some_list):
   quickSortHelper(some_list,0,len(some_list)-1)

def quickSortHelper(some_list,first,last):
   if first<last:

       splitpoint = partition(some_list,first,last)

       quickSortHelper(some_list,first,splitpoint-1)
       quickSortHelper(some_list,splitpoint+1,last)

#partition function implements the process described earlier.
def partition(some_list,first,last):
   pivotvalue = some_list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and some_list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while some_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = some_list[leftmark]
           some_list[leftmark] = some_list[rightmark]
           some_list[rightmark] = temp

   temp = some_list[first]
   some_list[first] = some_list[rightmark]
   some_list[rightmark] = temp


   return rightmark

quickSort(some_list)
print(some_list)

#heap sort
#http://varunpant.com/posts/heap-sort


def parent(i):
    return int(i/2)

def left(i):
    return 2 * i

def right(i):
    return left(i) + 1

def maxHeapify(some_list,i,sz):
    l = left(i)
    r = right(i)
    largest = None
    if l <= sz and some_list[l] > some_list[i]:
        largest = l
    else:
        largest = i

    if r <= sz and some_list[r] > some_list[largest]:
        largest = r

    if largest != i:
        temp = some_list[i]
        some_list[i] = some_list[largest]
        some_list[largest] = temp 
        maxHeapify(some_list,largest,sz)

def heapsort(some_list):
    heap_size = len(some_list)
    middle = int(heap_size/2)
    for i in range(middle,0,-1):
        maxHeapify(some_list,i,heap_size - 1)

    m = heap_size - 1
    for i in range(m,-1,-1): 
        temp = some_list[0]
        some_list[0] = some_list[i]
        some_list[i] = temp 
        m = m-1 
        maxHeapify(some_list,0,m)

heapsort(some_list)
print(some_list)