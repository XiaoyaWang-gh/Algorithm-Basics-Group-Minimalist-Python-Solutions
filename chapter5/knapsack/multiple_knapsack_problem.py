'''
多重背包：每个物品的个数是有限个

朴素版本
'''

M = 101
f = [[0]*M for _ in range(M)]
v = [0] * M
w = [0] * M
s = [0] * M

def main():
    N,V = map(int,input().split())
    for i in range(1,N+1):
        v[i],w[i],s[i] = map(int,input().split())

    for i in range(1,N+1):
        for j in range(1,V+1):
            for k in range(0,min(j//v[i],s[i])+1): # 和完全背包最大的区别就是k的终点需要考虑s[i]
                f[i][j] = max(f[i][j],f[i-1][j-k*v[i]]+k*w[i])

    print(f[N][V])

if __name__ == "__main__":
    main()