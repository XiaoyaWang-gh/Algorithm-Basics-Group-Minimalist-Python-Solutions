# 用数组模拟队列：先进先出

q = [0] * 100001
hh = 0 #队头
tt = -1 #队尾

def empty():
    global hh,tt
    if hh<=tt:
        print("NO")
    else:
        print("YES")

def push(x):
    global tt
    tt += 1
    q[tt] = x

def pop():
    global hh
    hh += 1

def query():
    print(q[hh])

def main():
    n = int(input())
    for _ in range(n):
        op = input().split()
        if op[0]=="push":
            push(int(op[1]))
        elif op[0]=="pop":
            pop()
        elif op[0]=="query":
            query()
        else:
            empty()

if __name__ == "__main__":
    main()