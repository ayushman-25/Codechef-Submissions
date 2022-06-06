n = int(input())
s1 = [int(input()) for _ in range(n)]
s2 = [int(input()) for _ in range(n)]
xor = [int(input()) for _ in range(n)]
orig = [s1[i] ^ xor[i] for i in range(n)]
print(*orig, sep='\n')
print(sum(abs(orig[i] - s2[i]) for i in range(n)))
