'''
两维的f是基础算法
一维是优化算法，注意内层循环降序
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
        for j in range(V,v[i]-1,-1):
            f[j] = max(f[j],f[j-v[i]]+w[i])

    print(f[V])

if __name__ == "__main__":
    main()