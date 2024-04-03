'''
https://www.nowcoder.com/practice/f350f14cd22c41aabfa7e54a1b8e8825?tpId=182&tqId=34610&ru=/exam/oj

1,2,3,4,5
1,5,2,4,3

思路：不需要用到链表，数组一分为二，前n/2正读，后n/2反读，输出到n个结束，尾逗号特殊处理
'''

def main():
    
    numbers = list(map(int, input().split(',')))
    num = len(numbers)
    head = 0
    tail = num-1
    while head<tail:
        print(numbers[head],end=',')
        if num // tail == 2 and num % tail == 0:
            print(numbers[tail],end='')
        else:
            print(numbers[tail],end=',')
        head += 1
        tail -= 1
    if num % 2 == 1:
        print(numbers[num//2])

if __name__ == "__main__":
    main()