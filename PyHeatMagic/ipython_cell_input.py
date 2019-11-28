def fibo_rec(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)


fibo_rec(22)

