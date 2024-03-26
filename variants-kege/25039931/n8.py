from itertools import product

words = []
for _ in product("ПРОСТО", repeat=6):
    if _.count('П') == 1 and _.count('Р') == 1 and _.count('О') == 2 and _.count('С') == 1 and _.count('Т') == 1:
        skip = False
        for index in range(1, 6):
            if _[index-1] == _[index]: skip = True
        if skip is False and _ not in words:
            print(_)
            words.append(_)


print(len(words))
