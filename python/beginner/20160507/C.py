# coding: utf-8;

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ta = sum([i for i in a[:n - k + 1]])
    res = ta
    l = 0

    for na in a[n - k + 1:]:
        ta = ta - int(a[l]) + int(na)
        res += ta
        l += 1

    print(res)

if __name__ == '__main__':
    main()
