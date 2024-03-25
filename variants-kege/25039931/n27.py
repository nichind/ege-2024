"""
Слишком долгий рантайм... (Ответ для A сходится)
"""
with open('variants-kege/25039931/27-B_12934.txt', 'r') as f:
    k = int(f.readline())
    water = f.read().split('\n')
    water = water[0:-1]

    max_len = 0
    water = [int(x) for x in water]
    for first in range(len(water)):
        cur = water[first]
        cur_len = 1
        for second in range(first + 1, len(water)):
            cur += water[second]
            if cur < k:
                cur_len += 1
                if cur_len > max_len: max_len = cur_len
            else:
                break

print(max_len)