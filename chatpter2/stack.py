# 用数组模拟栈：先进后出
tt = -1 # 表示栈顶
stk = [0] * 100001 # 存储栈中元素

def query():
    global tt
    print(stk[tt])
    return 

def push(x):
    global tt
    tt += 1
    stk[tt] = x
    

def pop():
    global tt
    tt -= 1

def empty():
    if tt==-1:
        print("YES")
    else:
        print("NO")

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
        