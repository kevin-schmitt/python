def bad_function(val, b = 5):
    if val<0:
        return - 1
    else:
        return b


if __name__ == '__main__':
    print(bad_function(3))