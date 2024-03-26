'''
最短编辑距离

集合：f[i][j]表示所有将a[1-i]变成b[1-j]的操作方式
属性：min (所有操作方式的操作次数的最小值)
划分：按照最后一步的操作方式 erase a[i],add,change
    分别对应f[i-1][j]+1,f[i][j-1]+1,f[i-1][j-1]+1 (其实没理解
    第三种要视情况而定
'''

M = 1001
f = [[0]*M for _ in range(M)]


def main():
    len_a = int(input())
    str_a = input()
    len_b = int(input())
    str_b = input()
    str_a = " "+str_a
    str_b = " "+str_b

    # 初始化边界
    for i in range(1,len_a+1):
        f[i][0] = i
    for j in range(1,len_b+1):
        f[0][j] = j
    
    for i in range(1,len_a+1):
        for j in range(1,len_b+1):
            f[i][j] = min(f[i-1][j],f[i][j-1]) + 1
            # 修改的情况视a[i]和b[j]是否相等而定
            if str_a[i] == str_b[j]:
                f[i][j] = min(f[i][j],f[i-1][j-1])
            else:
                f[i][j] = min(f[i][j],f[i-1][j-1]+1)

    print(f[len_a][len_b])


if __name__ == "__main__":
    main()