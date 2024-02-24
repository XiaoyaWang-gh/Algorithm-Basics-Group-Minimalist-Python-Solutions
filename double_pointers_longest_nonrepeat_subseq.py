

def main():
    len = int(input())
    seq = list(map(int, input().split()))
    longest_sub_len = 0
    num_lst = [0] * 100010

    j = 0 # j代表左端点
    for i in range(len): # i代表右端点
        # j和i都不走回头路
        num_lst[seq[i]] += 1
        while num_lst[seq[i]] > 1:
            num_lst[seq[j]] -= 1
            j += 1
        longest_sub_len = max(longest_sub_len, i-j+1)

    print(longest_sub_len)

if __name__ == "__main__":
    main()