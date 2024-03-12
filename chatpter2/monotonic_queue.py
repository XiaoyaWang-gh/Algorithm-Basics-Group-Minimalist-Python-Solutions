# 154. 滑动窗口
# 用队列来维护窗口

q1 = [0] * 1000001 # 存单调队列
q2 = [0] * 1000001 # 存单调队列


def main():
    n,k = map(int,input().split())
    v = list(map(int,input().split())) # 存原先值

    hh = 0 # 队头
    tt = -1 # 队尾
    for i in range(n): # i表示当前队列的终点

        # 判断队头是否已经滑出窗口
        if hh<=tt and i-k+1 > q1[hh]:
            hh += 1
        # 如果队尾大于刚加进来的数，那么删掉队尾
        while hh<=tt and v[q1[tt]] >= v[i]:
            tt -= 1

        tt += 1
        q1[tt] = i

        if i>=k-1: # 对于单调上升的队列，最小值一定在队头
            print(v[q1[hh]],end=' ')

    print() #换行

    hh = 0 # 队头
    tt = -1 # 队尾
    for i in range(n): # i表示当前队列的终点

        # 判断队头是否已经滑出窗口
        if hh<=tt and i-k+1 > q2[hh]:
            hh += 1
        # 如果队尾小于刚加进来的数，那么删掉队尾
        while hh<=tt and v[q2[tt]] <= v[i]:
            tt -= 1

        tt += 1
        q2[tt] = i

        if i>=k-1: # 对于单调下降的队列，最大值一定在队头
            print(v[q2[hh]],end=' ')
    




if __name__ == "__main__":
    main()