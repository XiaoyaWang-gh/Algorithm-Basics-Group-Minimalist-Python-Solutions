'''
合并石子
区间DP：状态表示的是某一个区间

集合：f[i][j]表示所有将第i堆石子到第j堆石子合并成一堆石子的合并方式
属性：min
划分：最后一次合并发生的位置

'''
import sys

M = 301
f = [[sys.maxsize]*M for _ in range(M)]
 
def main():
    N = int(input())
    s = list(map(int,input().split()))
    s = [0] + s
    acc_s = [0]*len(s)
    for i in range(1,len(s)): # 前缀和
        acc_s[i] = acc_s[i-1] + s[i]

    # 初始化状态方程
    for i in range(1,len(s)):
        f[i][i] = 0

    # 按照区间长度从小到大枚举
    for le in range(1,N+1):
        # 区间长度（le）     1   2     3
        # 起点最多能到(R)    N   N-1   N-2
        # le + R = N+1
        for i in range(1,N+2-le): # 按照区间左端点枚举
            l = i
            r = l + le -1
            for k in range(l,r):# k是最后一次合并时左边堆的右边界
                # 最后一次合并的开销是确定的 acc_s[j]-acc_s[i-1]
                f[l][r] = min(f[l][r],f[l][k]+f[k+1][r]+acc_s[r]-acc_s[l-1])

    print(f[1][N])

if __name__ == "__main__":
    main()