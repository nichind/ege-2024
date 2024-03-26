for i in range(3, 10001):
    n = '5' + '2'*i

    while '52' in n or '2222' in n or '1122' in n:
        if '52' in n:
            n = n.replace('52', '11')
        elif '2222' in n:
            n = n.replace('2222', '5')
        elif '1122' in n:
            n = n.replace('1122', '25')

    s = [x for x in list(n)]
    s = [int(x) for x in s]
    s = sum(s)

    if str(s)[-1] == '7':
        print(n)
        break