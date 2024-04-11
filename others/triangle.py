
def main():
    # nums = [2,3,4,4]
    nums = [1,2,3,4]
    sorted_nums = sorted(nums)
    n = len(nums)
    # total_num = n*(n-1)*(n-2)//6
    # tmp = 0
    # for i in range(0,n-2): # 0~n-3
    #     for j in range(i+1,n-1):# 1~n-2
    #         for k in range(n-1,j,-1): # n-1~2
    #             # print(sorted_nums[i],sorted_nums[j],sorted_nums[k])
    #             if sorted_nums[i] + sorted_nums[j] > sorted_nums[k]:
    #                 break
    #             tmp += 1
    # print(total_num-tmp)

    sn = sorted_nums
    first = 0
    last = n-1
    res = 0
    for first in range(0,n-2):
        for last in range(n-1,1,-1):
            second = first+1
            while sn[first] + sn[second] <= sn[last] and second < last:
                second += 1
            if sn[first] + sn[second] > sn[last] and second < last:
                print(first,second,last)
                res += last - second
    print(res)
        

if __name__ == "__main__":
    main()