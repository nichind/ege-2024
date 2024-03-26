with open('./17_12926.txt', 'r') as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    idata = [int(x) for x in data]

max_double_digit = 0
for n in sorted(idata):
    if n >= 100: break
    max_double_digit = n


max_sum_fourth = [-99999999]
for i in range(3, len(data)):
    if data[i-3][-1] == data[i][-1] and data[i-2][-1] == data[i][-1] and data[i-1][-1] == data[i][-1]:
        _ = sum([int(data[i-3]), int(data[i-2]), int(data[i-1]), int(data[i])])
        if _ > sum(max_sum_fourth):
            max_sum_fourth = [int(data[i-3]), int(data[i-2]), int(data[i-1]), int(data[i])]


A = sum(max_sum_fourth)
min_sum_fifth = 0
fifth_count = 0
for i in range(4, len(data)):
    less_count = 0
    for _ in [0,1,2,3,4]:
        if int(data[i-_]) < A: less_count += 1
    if less_count == 1 and sum([idata[i], idata[i-1], idata[i-2], idata[i-3], idata[i-4]]) % max_double_digit == 0:
        fifth_count += 1
        if sum([idata[i], idata[i-1], idata[i-2], idata[i-3], idata[i-4]]) < min_sum_fifth:
            min_sum_fifth = sum([idata[i], idata[i-1], idata[i-2], idata[i-3], idata[i-4]])

print(fifth_count, min_sum_fifth)