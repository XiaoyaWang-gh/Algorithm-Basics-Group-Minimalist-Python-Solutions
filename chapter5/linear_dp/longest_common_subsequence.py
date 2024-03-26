'''
给定两个字符串，求A和B的公共子序列的最大长度

集合：f[i][j] 所有由第一个序列前i个字母和第二个序列前j个字母构成的公共子序列
属性：Max
划分：本题难点
    A[i]和B[j]是否包含在子序列当中，分成4种情况10,01,00,11(00表示A[i]和B[j]都不选)
    00 f[i-1][j-1](省略，因为被第二类和第三类涵盖了，因此只写下面三种情况)
    11 f[i-1][j-1]+1
    01 f[i-1][j] (后者不等于前者，但是包含前者，求最大值结合划分可以重复)
    10 f[i][j-1]
'''

M = 1001
f = [[0]*M for _ in range(M)]

def main():
    
    len_a,len_b = map(int,input().split())
    str_a = input()
    str_b = input()
    str_a = " "+str_a
    str_b = " "+str_b

    for i in range(1,len_a+1):
        for j in range(1,len_b+1):
            f[i][j] = max(f[i-1][j],f[i][j-1])
            if str_a[i] == str_b[j]:
                    f[i][j] = max(f[i][j],f[i-1][j-1]+1)

    print(f[len_a][len_b])


if __name__ == "__main__":
    main()