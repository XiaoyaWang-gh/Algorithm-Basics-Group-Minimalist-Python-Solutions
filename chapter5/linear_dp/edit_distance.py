'''
编辑距离

直接定义最短编辑距离的函数会超时（同样的做法C++不会超时）

'''
M = 1001

def short_edit_distance(str_a,str_b):
    f = [[0]*M for _ in range(M)]

    len_a = len(str_a)
    len_b = len(str_b)
    str_a = " "+str_a
    str_b = " "+str_b

    # 初始化边界
    for i in range(1,len_a+1):
        f[i][0] = i
    for j in range(1,len_b+1):
        f[0][j] = j

    for i in range(1,len_a+1):
        for j in range(1,len_b+1):
            f[i][j] = min(f[i-1][j],f[i][j-1]) + 1
            # 修改的情况视a[i]和b[j]是否相等而定
            if str_a[i] == str_b[j]:
                f[i][j] = min(f[i][j],f[i-1][j-1])
            else:
                f[i][j] = min(f[i][j],f[i-1][j-1]+1)

    return f[len_a][len_b]

def main():
    str_num,query_num = map(int,input().split())
    al_lst = [] 
    for _ in range(str_num):
        al_s = input()
        al_lst.append(al_s)
    for _ in range(query_num):
        s,limit = input().split()
        limit = int(limit)
        cnt = 0
        for al_s in al_lst:
            if short_edit_distance(s,al_s) <= limit:
                cnt += 1
        print(cnt)

if __name__ == "__main__":
    main()