# 830. 单调栈
tt = -1 # 表示栈顶
stk = [0] * 100001 # 存储栈中元素

def main():
    global tt
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n):
        x = arr[i]
        while tt>-1 and stk[tt] >= x: # 删掉所有逆序点，得到严格单调上升的栈
            tt -= 1
        if tt>-1:
            print(stk[tt],end=" ")
        else:
            print(-1,end=" ")

        tt += 1
        stk[tt] = x

if __name__ == "__main__":
    main()