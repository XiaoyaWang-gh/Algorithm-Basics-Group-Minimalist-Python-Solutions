# Trie字符串统计

N = 100001

son = [[0]*26 for _ in range(N)]  # 第一维大小是N，表示父节点的idx，第二位大小是26，代表26个字母
cnt = [0] * N # 代表以当前的idx结尾的字符串的数量
idx = 0

def insert(s:str):
    global idx
    p = 0
    for i in range(len(s)):
        diff = ord(s[i])-ord('a')
        if son[p][diff] == 0:
            idx += 1
            son[p][diff] = idx
        p = son[p][diff]
    cnt[p] += 1


def query(s:str):
    p = 0
    for i in range(len(s)):
        diff = ord(s[i])-ord('a')
        if son[p][diff] == 0:
            print(0)
            return 
        p = son[p][diff]
    print(cnt[p])


def main():
    n = int(input())
    for _ in range(n):
        op = input().split()
        if op[0] == 'I':
            insert(op[1])
        else:
            query(op[1])

if __name__ == "__main__":
    main()