from sys import setrecursionlimit
setrecursionlimit(10**5)


def nya(n: int) -> int:
    if n == 1: return 1
    else: return n * nya(n - 1)


print(nya(2024) // nya(2022))
