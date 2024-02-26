
def main():
    n,m,q = map(int, input().split())
    arr = [[]]
    arr[0] = [0]*(m+1)
    for _ in range(n):
        arr.append([0]+list(map(int, input().split())))
    helper = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            helper[i][j] = arr[i][j] + helper[i-1][j] + helper[i][j-1] - helper[i-1][j-1]
    
    for _ in range(q):
        x1,y1,x2,y2 = map(int, input().split())
        print(helper[x2][y2] - helper[x1-1][y2] - helper[x2][y1-1] + helper[x1-1][y1-1])


if __name__ == "__main__":
    main()
