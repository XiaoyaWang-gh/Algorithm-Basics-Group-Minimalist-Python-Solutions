
def main():
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    helper = [0] * n
    for i in range(n):
        if i == 0:
            helper[i] = arr[i]
        else:
            helper[i] = helper[i-1] + arr[i]
    for _ in range(m):
        l,r = map(int, input().split())
        if l == 1:
            print(helper[r-1])
        else:
            print(helper[r-1] - helper[l-2])


if __name__ == "__main__":
    main()