# 数组模拟链表
# 827. 双链表  

head = -1 # 头节点的下标 / 头指针
tail = -1 # 尾节点的下标 / 尾指针
idx = 0 # 表示当前用到了哪个点
e = [0] * 100001 # 数据域，e[i]表示节点i的数据
ne = [-1] * 100001 # 指针域，ne[i]表示节点i的下一个节点的下标
prev = [-1] * 100001 # 指针域，prev[i]表示节点i的上一个节点的下标


def insert_to_head(x): # 及其常见的操作
    global idx, head, tail
    e[idx] = x
    ne[idx] = head
    prev[idx] = -1
    if head != -1:
        prev[head] = idx
    head = idx
    if tail == -1:
        tail = idx
    idx += 1

def insert_to_tail(x): # 及其常见的操作
    global idx, head, tail
    e[idx] = x
    ne[idx] = -1
    prev[idx] = tail
    if tail != -1:
        ne[tail] = idx
    tail = idx
    if head == -1:
        head = idx
    idx += 1

def delete_k(k): # 删除第k个插入的数
    global idx, head, tail
    if prev[k] != -1:
        ne[prev[k]] = ne[k]
    else:
        head = ne[k]
    if ne[k] != -1:
        prev[ne[k]] = prev[k]
    else:
        tail = prev[k]

def insert_after_k(k, x): # 将x插入到第k个插入的数后
    global idx, head, tail
    e[idx] = x
    ne[idx] = ne[k]
    prev[idx] = k
    if ne[k] != -1:
        prev[ne[k]] = idx
    else:
        tail = idx
    ne[k] = idx
    idx += 1

def insert_before_k(k, x): # 将x插入到第k个插入的数前
    global idx, head, tail
    e[idx] = x
    ne[idx] = k
    prev[idx] = prev[k]
    if prev[k] != -1:
        ne[prev[k]] = idx
    else:
        head = idx
    prev[k] = idx
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
        if op[0] == 'L':
            insert_to_head(int(op[1]))
        elif op[0] == 'R':
            insert_to_tail(int(op[1]))
        elif op[0] == 'D':
            k = int(op[1])
            delete_k(k-1)
        elif op[0] == 'IL':
            k, x = int(op[1]), int(op[2])
            insert_before_k(k-1, x)
        else:
            k, x = int(op[1]), int(op[2])
            insert_after_k(k-1, x)
    print_all()

if __name__ == "__main__":
    main()