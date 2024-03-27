'''
贪心：短视，每次都选择当前最优解，最后企图达到全局最优解

step 1 将区间按照右端点从小到大排序
step 2 将区间从前往后枚举，
    如果当前区间的已经包含点，则pass；
    如果当前区间还不包含点，则选择其右端点

'''

import sys

def main():
    n = int(input())
    interval_lst = []
    for _ in range(n):
        l,r = map(int,input().split())
        interval_lst.append((l,r))
    # 将区间按照右端点从小到大排序
    sorted_list = sorted(interval_lst,key=lambda x:x[1])
    
    # 初始化上一个点的坐标和点的总个数
    point, ans = -sys.maxsize, 0
    for interval in sorted_list:
        if interval[0] > point: # 如果当前区间的左端点严格大于上一个点
            point = interval[1]
            ans += 1
            
    print(ans)

if __name__ == "__main__":
    main()