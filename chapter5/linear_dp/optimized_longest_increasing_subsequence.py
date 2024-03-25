'''
最长上升子序列Ⅱ(优化版)

集合：f[i]表示以下标i作为结尾的上升子序列
属性：最长上升子序列的长度
分类：
    倒数第二个数字是第j个数字 0(没有倒数第二个数字),1,2,...,i-1
    存在冗余吗？

以下是ChatGPT的做法：二分+贪心
'''

def lengthOfLIS(nums):
    tails = []
    for x in nums:
        i, j = 0, len(tails)
        while i < j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
        print("tails :",tails)
    return len(tails)

def main():
    N = int(input())
    lst = list(map(int,input().split()))
    print(lengthOfLIS(lst))

if __name__ == "__main__":
    main()