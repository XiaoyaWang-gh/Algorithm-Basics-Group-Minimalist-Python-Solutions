


def main():
    n = float(input())
    if n > 1 or n < -1:
        if n > 0:
            l = 0
            r = n
        else:
            l = n
            r = 0
        while r-l > 1e-8:
            mid = (l+r)/2
            if mid*mid*mid > n:
                r = mid
            else:
                l = mid
        print(f"{l:.6f}")
    elif n != 0:
        if n > 0:
            l = 0
            r = 1
        else:
            l = -1
            r = 0
        while r-l > 1e-8:
            mid = (l+r)/2
            if mid*mid*mid < n:
                l = mid
            else:
                r = mid
        print(f"{l:.6f}")
    else:
        print(0.000000)


if __name__ == "__main__":
    main()