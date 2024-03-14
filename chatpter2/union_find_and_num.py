'''
# 837. 连通块中点的数量
在普通并查集的基础上，动态维护每个集合的元素个数
额外开辟数组 size[N] 代表每个集合的大小，只保证根节点的size有意义
'''

p = [0] * 100001
size = [1] * 100001

def find_root(x):
    if p[x] != x:
        p[x] = find_root(p[x])
    return p[x]


def merge(x,y):
    x = find_root(x)
    y = find_root(y)
    if x!=y: # 只有当它们不在同一个集合中才合并
        p[x] = y
        size[y] += size[x]

def query(x,y):
    x = find_root(x)
    y = find_root(y)
    if x == y:
        print('Yes')
    else:
        print('No')

def main():
    n,m = map(int,input().split())

    # 初始化:让所有的节点的p值等于自身
    for i in range(1,n+1):
        p[i] = i

    for _ in range(m):
        op = input().split()
        print(op)
        if op[0] == 'C':
            x = int(op[1])
            y = int(op[2])
            merge(x,y)
        elif op[0] == 'Q1':
            x = int(op[1])
            y = int(op[2])
            query(x,y)
        else:
            x = int(op[1])
            print(size[find_root(x)])

if __name__ == "__main__":
    main()