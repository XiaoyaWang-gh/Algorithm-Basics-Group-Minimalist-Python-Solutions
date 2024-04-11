'''
n皇后
https://www.acwing.com/problem/content/845/
'''

n = 0
path = [0] * 10
col_st = [0] * 10 # col_st[i]表示第i列有Q
anti_diag_st = [0] * 20 # anti_diag_st[i]表示第i条反对角线有Q
diag_st = [0] * 20 # diag_st[i]表示第i条对角线有Q

def print_line(x): # 打印Queen在位置x上的一行
    for i in range(1,n+1):
        if i != x:
            print(".",end="")
        else:
            print("Q",end="")
    print()

def dfs(x): # 第x+1行
    # print("x : ",x)
    if x == n:
        for i in range(n):
            print_line(path[i])
        print()
    for i in range(1,n+1):
        anti_diag = x+1-i+n
        diag = x+1+i
        if col_st[i] != 1 and anti_diag_st[anti_diag]!=1 and diag_st[diag] != 1:
            path[x] = i
            col_st[i] = anti_diag_st[anti_diag] = diag_st[diag] = 1
            dfs(x+1)
            col_st[i] = anti_diag_st[anti_diag] = diag_st[diag] = 0 # 恢复现场


def main():
    global n
    n = int(input())
    dfs(0)

if __name__ == "__main__":
    main()