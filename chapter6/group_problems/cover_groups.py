'''
尝试用贪心作答
Step 1 将所有区间按照左端点从小到大排序
Step 2 维护一个已经覆盖的线段区间，开始枚举每个区间
        如果当前区间满足以下要求：
            区间的左端点小于等于线段区间的右端点；
            区间的右端点大于线段区间的右端点
        放入备选区间
        在备选区间中选择右端点最大的区间，更新右端点
        否则放弃
        直至右端点达到指定的坐标
'''

def main():
    l,r = map(int,input().split())
    n = int(input())
    inter_lst = []
    for _ in range(n):
        il,ir = map(int,input().split())
        inter_lst.append((il,ir))

    # 排序
    sorted_lst = sorted(inter_lst,key=lambda x:x[0])
    
    # 判断最左端点和最右端点是否可能覆盖
    if sorted_lst[0][0] > l or sorted_lst[-1][1] < r:
        print(-1)
        return 
    
    # 初始化需要区间的个数
    ans = 0 
    # 初始化已覆盖区间的右端点
    cr = l
    # 维护初始化现阶段满足条件的所有区间的右端点的最大值
    max_r = l
    for interval in sorted_lst:
        if interval[0] <= cr and interval[1] > cr:
            if max_r < interval[1]:
                max_r = interval[1]
        else:
            if interval[1] < l: # 第一个满足条件的区间还没出现
                continue
            else: # 现阶段满足条件的所有区间结束了
                ans += 1
                cr = max_r
                if cr >= r:
                    break
    
    if cr < r:
        ans += 1

    print(ans)

if __name__ == "__main__":
    main()