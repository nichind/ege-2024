def f(start, final,
      flag=False):
    if start == 10:
        flag = True
    if (start == final) and flag:
        return 1
    if start > final or start == 11 or start == 12:
        return 0
    return f(start + 1, final, flag) + f(start * 2, final, flag) + f(start**2, final, flag)


print(f(2, 40))