


def quick_sort(arr, low, high):
    if low >= high:
        return
    
    # 三数取中法选择基准
    mid = low + (high - low) // 2
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    if arr[mid] > arr[low]:
        arr[mid], arr[low] = arr[low], arr[mid]

    x = arr[low]

    # 双指针法分区
    i = low-1
    j = high+1
    while i < j:
        while True:
            j -= 1
            if arr[j] <= x:
                break
        while True:
            i += 1
            if arr[i] >= x:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    quick_sort(arr, low, j)
    quick_sort(arr, j+1, high)
    


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, n - 1)
    print(*arr)


if __name__ == "__main__":
    main()