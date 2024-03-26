max_r = 0
for n in range(1000):
    binary = bin(n)
    print(binary)
    if n % 3 == 0:
        binary = '0b' + binary[2:].replace('0', '11')
    else:
        binary = '0b' + binary[2:].replace('1', '10')
    print(binary)
    r = int(binary, 2)
    if max_r < r <= 161 and r: max_r = r


print(max_r)
