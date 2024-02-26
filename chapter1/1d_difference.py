# 差分是前缀和的逆运算

def insert(b, l, r, c):
    b[l] += c
    b[r+1] -= c

def main():
    n,m = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] * (n+2)
    for i in range(1, n+1):
        insert(b, i, i, a[i])
    for _ in range(m):
        l,r,c = map(int, input().split())
        insert(b, l, r, c)
    for i in range(1, n+1):
        b[i] += b[i-1]
    print(*b[1:n+1])
        

    

if __name__ == "__main__":
    main()