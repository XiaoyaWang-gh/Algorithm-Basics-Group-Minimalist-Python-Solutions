'''
线性DP第一题
集合：f[i][j]所有从起点走到(i,j)的路径
属性：这些路径的和的最大值
分类：来自左上f[i-1][j-1]/正上f[i-1][j]

注意路径上的数字可以是负数，f状态方程一开始初始化为负无穷
'''

import sys

M = 501
t = [[0]*M for _ in range(M)]
f = [[-sys.maxsize]*M for _ in range(M)]

def main():

    N = int(input())
    for i in range(1,N+1):
        lst = list(map(int,input().split()))
        for j in range(1,i+1):
            t[i][j] = lst[j-1]

    for i in range(1,N+1):
        for j in range(1,i+1):
            if i-1>=1 and j-1>=1: # 从正上方或者左上方来
                f[i][j] = max(f[i-1][j-1],f[i-1][j]) + t[i][j]
            elif i-1>=1 and j == 1: # 从正上方来
                f[i][j] = f[i-1][j] + t[i][j]
            else: # 本身是起点
                f[i][j] = t[i][j]

    ans = max(f[N][1:N+1])

    print(ans)


if __name__ == "__main__":
    main()