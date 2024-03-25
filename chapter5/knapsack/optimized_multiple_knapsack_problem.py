'''
多重背包：每个物品的个数是有限个

优化版本

回忆完全背包优化思路
对比f[i][j]和f[i][j-v]来源的集合，但是f[i][j-v]比f[i][j]多了一项
不能直接用完全背包优化思路

"二进制优化"方式：
假如s[i]=1023，可以把第i个物品打包成十组考虑1，2，4，...，512
这10组可以拼凑成0~1023当中的任何一个数字
可以枚举这10组选和不选的情况
如果s[i]=200,那么拆成1,2,4,8,16,32,64,73(128大咩)
S -> logS
对所有新的分组做一下01背包
'''
import math

M = 1000 * math.ceil(math.log2(2000)) # 按说开到这么大就够了，但实际不行，还要再乘十
v = [0] * M
w = [0] * M
f = [0] * M


def main():
    N,V = map(int,input().split())
    cnt = 1
    for i in range(1,N+1):
        a,b,s = map(int,input().split())
        k = 1
        while k <= s:
            v[cnt] = k*a
            w[cnt] = k*b
            s -= k
            k *= 2
            cnt += 1
        if s>0:
            v[cnt] = s*a
            w[cnt] = s*b
            cnt += 1
    
    for i in range(1,cnt): # 物品数量一共是cnt-1
        for j in range(V,v[i]-1,-1):
            f[j] = max(f[j],f[j-v[i]]+w[i])

    print(f[V])

if __name__ == "__main__":
    main()