'''
完全背包：每件物品可以用无限多次

朴素做法 Time Limit Exceeded

该优化解法和01背包唯一的区别是max的第二个参数的第一维
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
            f[i][j] = f[i-1][j] # 第i件物品不放入
            if j>=v[i]: # 第i件物品放入的是有前提条件的
                f[i][j] = max(f[i][j],f[i][j-v[i]]+w[i]) # 和01背包唯一的区别是max的第二个参数的第一维

    print(f[N][V])

if __name__ == "__main__":
    main()