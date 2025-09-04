import bisect

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    print(bisect.bisect_right(l, 3))