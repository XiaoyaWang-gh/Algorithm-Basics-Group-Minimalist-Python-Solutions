'''
区间分组

Step 1 将所有区间按照左端点从小到大排序
Step 2 依次枚举每一个区间，判断是否有分组可以收留这个区间，
       即判断是否有分组的最右点是小于这个区间的左端点的
       如有，加入分组，更新最右点的最小值
       如没有，开创新组
       
'''


import heapq # 用于将普通列表转化成一个最小堆

def main():
    n = int(input())
    interval_lst = []
    for _ in range(n):
        l,r = map(int,input().split())
        interval_lst.append((l,r))
    # 将区间按照左端点从小到大排序
    sorted_list = sorted(interval_lst,key=lambda x:x[0])
    
    # 初始化存放每个区间的最右点坐标的数组(优先队列)
    r_coords = []

    for interval in sorted_list:
        if len(r_coords) == 0 or r_coords[0] >= interval[0]: # 如果堆顶也大于等于区间左端点
                heapq.heappush(r_coords,interval[1])
        else:
            heapq.heappop(r_coords)
            heapq.heappush(r_coords,interval[1])

    print(len(r_coords))

if __name__ == "__main__":
    main()