
def insert(b, x1, y1, x2, y2, v):
    b[x1][y1] += v
    b[x1][y2+1] -= v
    b[x2+1][y1] -= v
    b[x2+1][y2+1] += v

def main():
    n,m,q = map(int, input().split())
    a = [[]]
    b = [[0]*(m+2) for _ in range(n+2)]
    a[0] = [0]*(m+1)
    for _ in range(n):
        a.append([0]+list(map(int, input().split())))
    for i in range(1, n+1):
        for j in range(1, m+1):
            insert(b, i, j, i, j, a[i][j])
    for _ in range(q):
        x1,y1,x2,y2,v = map(int, input().split())
        insert(b, x1, y1, x2, y2, v)
    for i in range(1, n+1):
        for j in range(1, m+1):
            b[i][j] = b[i][j] + b[i-1][j] + b[i][j-1] - b[i-1][j-1]

    for i in range(1, n+1):
        print(*b[i][1:m+1])


if __name__ == "__main__":
    main()