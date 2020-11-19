for _ in range(int(input())):
    days, day = input().split()
    days = int(days)
    l1 = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
    if l1[0] == day:
        if days == 28:
            print('4 4 4 4 4 4 4')
        elif days == 29:
            print('5 4 4 4 4 4 4')
        elif days == 30:
            print('5 5 4 4 4 4 4')
        elif days == 31:
            print('5 5 5 4 4 4 4')
    elif l1[1] == day:
        if days == 28:
            print('4 4 4 4 4 4 4')
        elif days == 29:
            print('4 5 4 4 4 4 4')
        elif days == 30:
            print('4 5 5 4 4 4 4')
        elif days == 31:
            print('4 5 5 5 4 4 4')
    elif l1[2] == day:
        if days == 28:
            print('4 4 4 4 4 4 4')
        elif days == 29:
            print('4 4 5 4 4 4 4')
        elif days == 30:
            print('4 4 5 5 4 4 4')
        elif days == 31:
            print('4 4 5 5 5 4 4')
    elif l1[3] == day:
        if days == 28:
            print('4 4 4 4 4 4 4')
        elif days == 29:
            print('4 4 4 5 4 4 4')
        elif days == 30:
            print('4 4 4 5 5 4 4')
        elif days == 31:
            print('4 4 4 5 5 5 4')
    elif l1[4] == day:
        if days == 28:
            print('4 4 4 4 4 4 4')
        elif days == 29:
            print('4 4 4 4 5 4 4')
        elif days == 30:
            print('4 4 4 4 5 5 4')
        elif days == 31:
            print('4 4 4 4 5 5 5')
    elif l1[5] == day:
        if days == 28:
            print('4 4 4 4 4 4 4')
        elif days == 29:
            print('4 4 4 4 4 5 4')
        elif days == 30:
            print('4 4 4 4 4 5 5')
        elif days == 31:
            print('5 4 4 4 4 5 5')
    elif l1[6] == day:
        if days == 28:
            print('4 4 4 4 4 4 4')
        elif days == 29:
            print('4 4 4 4 4 4 5')
        elif days == 30:
            print('5 4 4 4 4 4 5')
        elif days == 31:
            print('5 5 4 4 4 4 5')