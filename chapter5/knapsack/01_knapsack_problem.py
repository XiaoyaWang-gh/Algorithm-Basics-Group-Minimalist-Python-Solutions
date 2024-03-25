'''
01背包：每件物品最多只能用一次

DP考虑角度：

1.状态表示：思考整个问题需要几维表示，f(i,j)表示什么
每个状态都是一个集合，存放的数是集合的属性(max,min,cnt)
条件：只从前i个物品中选，总体积<=j

2.状态计算：f(i,j)怎么计算
对应集合的划分，如何将当前的集合划分成若干个子集，每个子集都可以算出
对于01knapsack，分成：含i和不含i
f(i,j) = max(f(i-1,j),f(i-1,j-v_i)+w_i)
子集的划分原则：不重不漏(求最大值时不重可以不满足)

DP问题优化：
对DP的代码或计算方程做等价变形

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
                f[i][j] = max(f[i][j],f[i-1][j-v[i]]+w[i])

    print(f[N][V])

if __name__ == "__main__":
    main()