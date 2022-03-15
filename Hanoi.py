def hanoi(n, cur, empty, des):
    if n == 1:
        print(cur, '--->', des)
    else:
        hanoi(n-1, cur, des, empty)
        print(cur, '--->', des)
        hanoi(n-1, empty, cur, des)
