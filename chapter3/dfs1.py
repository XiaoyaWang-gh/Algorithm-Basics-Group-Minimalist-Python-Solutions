'''
深搜
https://www.acwing.com/problem/content/844/
全排列 
'''

n = 0
path = [0] * 10
st = [0] * 10 # st[i]为1表示数字i已经在当前路径上被输出

def dfs(x):
    if x == n:
        for i in range(n):
            print(path[i],end=' ')
        print()
    for i in range(1,n+1):
        if st[i] != 1:
            path[x] = i
            st[i] = 1
            dfs(x+1)
            st[i] = 0


def main():
    global n
    n = int(input())
    dfs(0)

if __name__ == "__main__":
    main()