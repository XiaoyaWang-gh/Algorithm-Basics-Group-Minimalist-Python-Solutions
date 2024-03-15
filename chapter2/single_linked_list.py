# 数组模拟链表
# 826. 单链表 
# 最常出现的单链表：邻接表(多链表)，用途：存储树和图
# 双链表常见用途：优化某些问题

# 每个节点存储两个信息：数据元素，存在数组e中，下一个节点的位置/下标，存在数组ne中

head = -1 # 头节点的下标
idx = 0 # 表示当前用到了哪个点
e = [0] * 100001 # 数据域，e[i]表示节点i的数据
ne = [0] * 100001 # 指针域，ne[i]表示节点i的下一个节点的下标

def insert_to_head(x): # 及其常见的操作
    global idx, head
    e[idx] = x
    ne[idx] = head
    head = idx
    idx += 1

def delete_after_k(k): # 删除第k个插入的数后面的数
    global idx
    ne[k] = ne[ne[k]]

def insert_after_k(k, x): # 将x插入到第k个插入的数后
    global idx
    e[idx] = x
    ne[idx] = ne[k]
    ne[k] = idx 
    idx += 1

def print_all():
    i = head
    while i != -1:
        print(e[i], end=' ')
        i = ne[i]
    print()

def main():
    n = int(input())
    while n:
        n -= 1
        op = input().split()
        if op[0] == 'H':
            insert_to_head(int(op[1]))
        elif op[0] == 'D':
            k = int(op[1])
            if k == 0:
                global head
                head = ne[head]
            else:
                delete_after_k(k - 1)
        else:
            k, x = int(op[1]), int(op[2])
            insert_after_k(k - 1, x)
    print_all()

if __name__ == "__main__":
    main()