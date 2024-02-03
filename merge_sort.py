

def merge_sort(arr, l, r):
    if l >= r:
        return
    
    mid = (l + r) // 2

    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)

    i = l
    j = mid + 1
    temp = [] # 归并排序需要开辟临时数组，快排则不需要
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= r:
        temp.append(arr[j])
        j += 1
    k = 0
    for i in range(l, r + 1):
        arr[i] = temp[k]
        k += 1


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    merge_sort(arr, 0, n - 1)
    print(*arr)


if __name__ == "__main__":
    main()