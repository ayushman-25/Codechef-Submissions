bin_n = list(bin(int(input()))[2:][::-1])
if sum(i == '1' for i in bin_n[0::2]) < sum(i == '1' for i in bin_n[1::2]):
    for i in range(0, len(bin_n), 2):
        bin_n[i] = '0'
else:
    for i in range(1, len(bin_n), 2):
        bin_n[i] = '0'
print(int("".join(bin_n[::-1]), 2))