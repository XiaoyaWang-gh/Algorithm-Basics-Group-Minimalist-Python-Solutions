

def main():
    len = int(input())
    seq = list(map(int, input().split()))
    longest_sub_len = 0
    num_lst = [0] * 100010 # 用于记录每个数字出现的次数

    j = 0 # j代表左端点
    for i in range(len): # i代表右端点
        # j和i都不走回头路
        num_lst[seq[i]] += 1 # 每次新加的数字是seq[i]
        while num_lst[seq[i]] > 1: 
            num_lst[seq[j]] -= 1 # 每次减少的数字是seq[j]
            j += 1
        longest_sub_len = max(longest_sub_len, i-j+1)

    print(longest_sub_len)

if __name__ == "__main__":
    main()