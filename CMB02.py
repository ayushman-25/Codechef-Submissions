for x in range(int(input())):
    x = int(input())
    while(1):
    	x += 1
        if str(x) == str(x)[::-1]:
            print(x)
            break