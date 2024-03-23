'''
124. 数的进制转换
思路：以十进制作为R进制和S进制之间的媒介
R进制转十进制：easy to think
十进制转R进制：除基取余，最后翻转
'''

def _turn_char_to_decimal_num(ch)->int:
    if ch >= '0' and ch <= '9':
        return int(ch)
    elif ch >= 'a' and ch <= 'z':
        return int(ord(ch)-ord('a')+36)
    else:
        return int(ord(ch)-ord('A')+10)
    
def _turn_decimal_num_to_char(num)->str:
    if num >= 0 and num <= 9:
        return str(num)
    elif num >= 10 and num <= 35:
        return chr(num-10+ord('A'))
    else:
        return chr(num-36+ord('a'))

def _convert_base_R_to_decimal(num:str,r:int)->int:
    num_d = 0
    l = len(num)
    for i in range(l):
        base = _turn_char_to_decimal_num(num[l-1-i])
        e = i
        num_d += base * (r ** e)
    # print("num_d:",num_d)
    return num_d

def _convert_decimal_to_base_R(num:int,r:int)->str:
    num_r = ""
    while num:
        num_r += _turn_decimal_num_to_char(num%r)
        num = num // r
    num_r = num_r[::-1]
    # print("num_r:",num_r)
    if num_r == "":
        return "0"
    return num_r

def convert_base_R_to_base_S(num_r:str,r:int,s:int)->str:
    num_d = _convert_base_R_to_decimal(num_r,r)
    num_s = _convert_decimal_to_base_R(num_d,s)
    return num_s

def main():
    n = int(input())
    for _ in range(n):
        r,s,num_r = input().split()
        r = int(r)
        s = int(s)
        print(r,num_r)
        num_s = convert_base_R_to_base_S(num_r,r,s)
        print(s,num_s)
        print()

if __name__ == "__main__":
    main()