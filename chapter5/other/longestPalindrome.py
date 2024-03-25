

def main():
    s = input()
    l = len(s)

    dp = [[0]*l for _ in range(l)]

    # 对角线的结果并不会被后面的状态参考，所以忽略初始化

    # 初始化最大长度
    max_len = 1
    for j in range(1,l):
        for i in range(0,j):
            if s[i]!=s[j]:
                dp[i][j] = 0
            else:
                if j-i < 3:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j-1]
            if dp[i][j] and j-i+1 > max_len:
                max_len = j-i+1
    
    print(max_len)


if __name__ == "__main__":
    main()