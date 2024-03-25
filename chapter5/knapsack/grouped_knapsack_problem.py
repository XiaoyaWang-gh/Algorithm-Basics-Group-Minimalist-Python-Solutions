'''
分组背包：物品分成n组，每组最多选一个物品

集合划分：f[i,j] 第i组的物品选哪个(不选也是一个子集)
    一个不选 ： f[i-1,j]
    选则第k个 ： f[i-1,j-v[i][k]]+w[i][k]

朴素写法
'''

M = 101
v = [[0]*M for _ in range(M)]
w = [[0]*M for _ in range(M)]
s = [[0]*M for _ in range(M)]
f = [[0]*M for _ in range(M)]

def main():
    N,V = map(int,input().split())
    for i in range(1,N+1):
        s[i] = int(input())
        for j in range(1,s[i]+1):
            v[i][j],w[i][j] = map(int,input().split())

    for i in range(1,N+1):
        for j in range(1,V+1):
            f[i][j] = f[i-1][j] # 第i组的物品一个都不选
            for k in range(1,s[i]+1):
                if j >= v[i][k]: # 选择第i组的第k个物品有前提条件
                    f[i][j] = max(f[i][j],f[i-1][j-v[i][k]]+w[i][k])

    print(f[N][V])

if __name__ == "__main__":
    main()