

def find_left_bound(n,arr,x):
    l = 0
    r = n-1
    while l<r:
        mid = (l+r)//2
        if arr[mid] >= x:
            r = mid
        else:
            l = mid+1
    return l if arr[l] == x else -1

def find_right_bound(n,arr,x):
    l = 0
    r = n-1  
    while l<r:
        mid = (l+r+1)//2
        if arr[mid] <= x:
            l = mid
        else:
            r = mid-1
    return r if arr[r] == x else -1

def binary_search(n,arr,x):
    left_idx = find_left_bound(n,arr,x)
    if left_idx == -1:
        print(-1,-1)
        return
    right_idx = find_right_bound(n,arr,x)
    print(left_idx,right_idx)


def main():
    n,q = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(q):
        x = int(input())
        binary_search(n,arr,x)

if __name__ == "__main__":
    main()