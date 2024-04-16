'''
线段树简单题 : 清点人数
https://www.acwing.com/file_system/file/content/whole/index/content/4184202/
'''
n = 0
bit = [0] * 505050

def lowbit(x)->int:
    return  x & -x

def single_point_add(m,p):
    while m <= n:
        bit[m] += p
        m += lowbit(m)
    return

def single_point_sub(m,p):
    while m <= n:
        bit[m] -= p
        m += lowbit(m)
    return

def check_before_m(m):
    ans = 0
    while m:
        ans += bit[m]
        m -= lowbit(m)
    return ans

def main():
    global n
    n,k = map(int,input().split())
    for _ in range(k):
        inputs = input().split()
        if inputs[0] == 'A':
            m = int(inputs[1])
            print(check_before_m(m))
        elif inputs[0] == 'B':
            m = int(inputs[1])
            p = int(inputs[2])
            single_point_add(m,p)
        else:
            m = int(inputs[1])
            p = int(inputs[2])
            single_point_sub(m,p)


if __name__ == "__main__":
    main()