from functools import lru_cache

'''
    Example of cache for better performance with algo of fibonachi
    you can test performance with timeit(10, 31) and timeit(25,42)
'''
@lru_cache()
def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

def sum(start, stop):
    result = 0
    for n in range(start, stop):
        result += fibo(n)
    return result

if __name__ == '__main__':
    print(sum(10, 31))
    print(sum(25, 42))