'''
完全背包：每件物品可以用无限多次

将状态转移方程降到一维，但是不同于01背包，内层循环无需倒序
'''

M = 1001
f = [0]*M
v = [0]*M
w = [0]*M


def main():
    
    N,V = map(int,input().split())
    for i in range(1,N+1):
        v[i],w[i] = map(int,input().split())

    for i in range(1,N+1):
        for j in range(v[i],V+1): # 不同于01背包，不需要倒序
            f[j] = max(f[j],f[j-v[i]]+w[i]) # 和01背包完全相同

    print(f[V])

if __name__ == "__main__":
    main()