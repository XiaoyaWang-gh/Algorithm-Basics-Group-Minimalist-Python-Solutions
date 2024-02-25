# 803. 区间合并
# Step1 : 区间排序
# Step2 : 维护区间

def main():
    n = int(input())
    intervals = []
    for _ in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r))
    intervals.sort()
    
    merged = []
    for l, r in intervals:
        if not merged or merged[-1][1] < l:
            merged.append((l, r))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], r))
    
    print(len(merged))

if __name__ == "__main__":
    main()
