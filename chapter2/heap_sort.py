'''
如何手写一个堆，堆维护了一个数据集合
----------------------------------------
基操：
1. 插入一个数   
    heap[++size] = x
    up(size)
2. 求集合当中的最小值
    heap[1]
3. 删除最小值(用堆的最后一个元素覆盖堆顶，再down对顶)
    一维数组删除头节点很困难，删除尾节点很容易
    heap[1] = heap[size]
    size --
    down(1)
4. 删除任意一个元素
    heap[k] = heap[size]
    size --
    down(k)
    up(k)
5. 修改任意一个元素
    heap[k] = x
    down(k)
    up(k)
----------------------------------------
堆是一个完全二叉树
小根堆：每个点的值都小于等于左右儿子
堆的存储：
一维数组，根节点存在1，x的左儿子2x，右儿子2x+1
建堆：
先不管大小按顺序存进数组，然后从n/2处开始倒叙到1进行down操作
----------------------------------------
down x: 
往下调整，发生在某个点的值变大时
up x:
往上调整，发生在某个点的值变小时
----------------------------------------
O(n) 的建堆方式(逐个插入的复杂度是O(nlogn))
'''

heap = [0] * 100001
size = 0

def up(k):
    t = k
    if k//2 >= 1 and heap[k//2] < heap[t]:
        t = k//2
    if t != k:
        v = heap[t]
        heap[t] = heap[k]
        heap[k] = v
        up(t)


'''
def up(k):
    while k//2 >= 1 and heap[k//2] < heap[t]:
        v = heap[t]
        heap[t] = heap[k]
        heap[k] = v
        k = k // 2
'''
        

def down(k):
    t = k
    if 2*k <= size and heap[2*k] < heap[t]:
        t = 2*k
    if 2*k+1 <= size and heap[2*k+1] < heap[t]:
        t = 2*k+1
    # 至此t是三者中的最小值
    if t != k:
        v = heap[t]
        heap[t] = heap[k]
        heap[k] = v
        down(t)

def main():
    n,m = map(int,input().split())
    global size,heap
    heap = [0] + list(map(int,input().split()))
    size = n
    # 建堆
    for i in range(n//2,0,-1):
        down(i)
    # for i in range(1,n+1):
    #     print(heap[i],end = ' ')
    # print()

    # 依次返回堆顶，删除堆顶
    for _ in range(m):
        print(heap[1],end = ' ')
        heap[1] = heap[size]
        size -= 1
        down(1)


if __name__ == "__main__":
    main()

'''
Input:
10 5
40 2 33 26 35 8 8 26 29 2
Answer:
2 2 8 8 26
'''