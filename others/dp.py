
def main():
    s = "aba"
    n = len(s)
    s = " "+s
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n):
        dp[i][i] = 1
    for i in range(n-1,0,-1):
        for j in range(1,n):
            if i <= j:
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i+1][j-1]+1,dp[i][j])
                    print("i = ",i,"j = ",j,"dp[i][j] = ",dp[i][j])
                        
    print(dp[1][n])

if __name__ == "__main__":
    main()