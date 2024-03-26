with open('./9.txt', 'r') as f:
    data = f.readlines()
    data = [x.replace('\n', '').split('\t') for x in data]


count = 0
for line in data:
    line = [int(x) for x in line]

    dd_nums = []
    for i in line:
        if line.count(i) == 2 and i not in dd_nums: dd_nums.append(i)

    if len(dd_nums) == 2 and max(line) not in dd_nums and (max(line) * min(line)) > (sum(line) - (max(line) + min(line))):
        print(sum(line))
        break
