for __ in range(int(input())):
    d = dict()
    for j in range(4):
        a, b = input().split()
        d[a] = int(b)
    if (d['Barcelona'] > d['Eibar'] and d['RealMadrid'] < d['Malaga']):
        print("Barcelona")
    else:
        print("RealMadrid")