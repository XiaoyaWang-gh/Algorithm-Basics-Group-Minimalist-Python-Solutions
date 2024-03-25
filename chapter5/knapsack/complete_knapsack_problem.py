'''
完全背包：每件物品可以用无限多次

和01背包的区别在于状态计算时集合划分不同
按照第i个物品选多少个分成若干组，如果第i个物品选了k个：
step 1:去掉k个第i个物品
step 2:求去完之后的最大值
step 3:加上k个第i个物品的价值
f[i-1][j-k*v[i]] + k*w[i]
f[i-1][j] 可以合并到上面的公式 f[i-1][j-0*v[i]] + 0*w[i]
注意k是可计算的
'''

M = 1001
f = [[0]*M for _ in range(M)]
v = [0]*M
w = [0]*M


def main():
    
    N,V = map(int,input().split())
    for i in range(1,N+1):
        v[i],w[i] = map(int,input().split())

    for i in range(1,N+1):
        for j in range(1,V+1):
            for k in range(0,j//v[i]+1):
                f[i][j] = max(f[i][j],f[i-1][j-k*v[i]] + k*w[i])

    print(f[N][V])

if __name__ == "__main__":
    main()