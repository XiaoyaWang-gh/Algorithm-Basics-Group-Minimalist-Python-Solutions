'''
# 836. 合并集合
一共有 n 个数，编号是 1∼n，最开始每个数各自在一个集合中。
现在要进行 m 个操作，操作共有两种：
M a b，将编号为 a 和 b 的两个数所在的集合合并，如果两个数已经在同一个集合中，则忽略这个操作；
Q a b，询问编号为 a 和 b 的两个数是否在同一个集合中；

基本原理：用树的形式维护所有的集合，根节点元素的idx是当前集合的编号，每个节点都存储父节点的idx(使用数组p)
1 - 根节点：p[x] == x
2 - 求x的集合编号：
while p[x] != x:
    x = p[x]
3 - 如何合并两个集合
p[x] = y | p[y] = x

并查集的优化：
在find_root方法中加上路径压缩

'''

p = [0] * 100001  # p[i]是i的祖先节点

def find_root(x):
    if p[x] != x:
        p[x] = find_root(p[x])
    return p[x]


def merge(x,y):
    x = find_root(x)
    y = find_root(y)
    if x!=y: # 只有当它们不在同一个集合中才合并
        p[x] = y

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
        x = int(op[1])
        y = int(op[2])
        if op[0] == 'M':
            merge(x,y)
        else:
            query(x,y)

if __name__ == "__main__":
    main()