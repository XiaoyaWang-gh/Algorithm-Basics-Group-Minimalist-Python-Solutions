# 830. 单调栈
# 给定一个长度为 N 的整数数列，输出每个数左边第一个比它小的数，如果不存在则输出 −1。
# 每个元素都出栈入栈一次，时间复杂度为O(n)
tt = -1 # 表示栈顶
stk = [0] * 100001 # 存储栈中元素

def main():
    global tt
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n):
        x = arr[i]
        while tt>-1 and stk[tt] >= x: # 删掉所有逆序点，得到严格单调上升的栈
            tt -= 1 # 弹栈
        if tt>-1:
            print(stk[tt],end=" ")
        else:
            print(-1,end=" ")

        tt += 1
        stk[tt] = x # 压栈

if __name__ == "__main__":
    main()