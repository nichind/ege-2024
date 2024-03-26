with open('./22.txt', 'r') as f:
    data = [x.replace('\n', '').split('\t') for x in f.readlines()]
    print(data)