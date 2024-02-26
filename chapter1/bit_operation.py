

def turn_binary(num):
    '''
    十进制转二进制
    '''
    # return bin(num)
    res = ''
    while num:
        res = str(num % 2) + res
        num = num // 2
    return res


def main():
    n = int(input())
    num_lst = list(map(int, input().split()))
    for i in range(n):
        num = num_lst[i]
        bin_str = turn_binary(num)
        print(bin_str.count('1'),end='')
        if i != n-1:
            print(' ',end='')


if __name__ == "__main__":
    main()