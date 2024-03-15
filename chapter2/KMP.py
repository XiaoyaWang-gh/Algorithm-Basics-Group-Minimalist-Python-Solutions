'''
给定一个字符串 S ，以及一个模式串 P ，所有字符串中只包含大小写英文字母以及阿拉伯数字。

模式串 P 在字符串 S 中多次作为子串出现。

求出模式串 P 在字符串 S 中所有出现的位置的起始下标。

KMP保证不会回溯

pattern abcdabd
prefix a,ab,abc,abcd,abcda,abcdab
suffix d,bd,abd,dabd,cdabd,bcdabd
观察前缀是否出现在字符串中的其他地方

部分匹配表如何产生？(next数组)
部分匹配值："前缀"和"后缀"的最长的共有元素的长度
a b c d a b d
0 0 0 0 1 2 0

最少移动位数 = 已匹配的字符数 - 对应的部分匹配值

'''


def main():
    n = int(input())
    p = input()
    m = int(input())
    s = input()

    # 求部分匹配表next的过程
    next = [0] * n
    j = 0
    for i in range(n):
        while j and p[i]!=p[j+1]:
            j = next[j]
        if p[i] == p[j+1]:
            j += 1
        next[i] = j
        
    # 匹配过程
    
    