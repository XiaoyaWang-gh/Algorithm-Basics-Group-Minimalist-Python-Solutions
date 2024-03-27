'''
贪心：短视，每次都选择当前最优解，最后企图达到全局最优解

step 1 将区间按照右端点从小到大排序
step 2 将区间从前往后枚举，如果当前区间的已经包含点，则pass；如果当前区间还不包含点，则选择其右端点

'''

def main():
    n = int(input())
    interval_lst = []
    for _ in range(n):
        l,r = map(int,input().split())
        interval_lst.append((l,r))
    # 将区间按照右端点从小到大排序
    sorted_list = sorted(interval_lst,key=lambda x:x[1])
    # 初始化点集
    points = [sorted_list[0][1]]
    # 初始化一个指针，不断向右移动，用来判断区间内是否包含某个点
    pp = 0
    # 按照区间从左往右枚举
    for interval in sorted_list[1:]:
        flag = False
        while pp < len(points):
            if points[pp] >= interval[0] and points[pp] <= interval[1]:
                flag = True
                break
            elif points[pp] > interval[1]:
                break
            else:
                pp += 1
        if not flag:
            points.append(interval[1])
    
    print(len(points))

if __name__ == "__main__":
    main()