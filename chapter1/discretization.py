# 802. 区间和
# 离散化：值域跨度大，但是密度稀疏

def main():
    n, m = map(int, input().split())
    events = [] # n+2m
    queries = [] # m
    for _ in range(n):
        x, c = map(int, input().split())
        events.append((x, c))
    for _ in range(m):
        l, r = map(int, input().split())
        queries.append((l, r))
        events.append((l, 0))
        events.append((r, 0))

    # 离散化
    unique_x = sorted(set(x for x, _ in events))
    index = {x: i for i, x in enumerate(unique_x)}

    # 差分数组
    diff = [0] * (len(unique_x) + 1)
    for x, c in events[:n]:
        diff[index[x]] += c

    # 构建前缀和
    for i in range(1, len(diff)):
        diff[i] += diff[i-1]

    # 查询结果
    for l, r in queries:
        print(diff[index[r]] - diff[index[l]-1] if index[l] > 0 else diff[index[r]])

if __name__ == "__main__":
    main()
