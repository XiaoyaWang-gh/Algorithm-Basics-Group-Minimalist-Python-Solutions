'''
堆排序
为第k大的元素铺垫
'''

import heapq

heap = [5,9,6,7,4,3,2]

heapq.heapify(heap)

while heap:
    print(heapq.heappop(heap))