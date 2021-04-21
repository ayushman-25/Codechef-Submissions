for i in range(int(int(input()) ** (1 / 3)), int(int(input()) ** (1 / 3)) + 1):
    if(len(set(str(i))) == 1 and str(i ** 3) != str(i ** 3)[::-1] and i > 9):
        print(i ** 3, i, sep='\t')