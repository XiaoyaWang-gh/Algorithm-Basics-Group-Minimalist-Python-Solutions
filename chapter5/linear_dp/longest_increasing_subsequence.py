'''
最长上升子序列Ⅰ(朴素版)

集合：f[i]表示以下标i作为结尾的上升子序列
属性：最长上升子序列的长度
分类：
    倒数第二个数字是什么 0(没有倒数第二个数字),1,2,...,i-1

'''
import sys

M = 1001
a = [sys.maxsize]*M
f = [1]*M

def main():
    N = int(input())
    lst = list(map(int,input().split()))
    for i in range(1,N+1):
        a[i] = lst[i-1]

    for i in range(2,N+1):
        for j in range(1,i):
            if a[i] > a[j]:
                f[i] = max(f[i],f[j]+1)
    print(max(f[1:N+1]))

if __name__ == "__main__":
    main()