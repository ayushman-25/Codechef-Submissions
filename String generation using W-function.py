s = input()
print(*[chr(ord('a') - 1 + int(i)) for i in s], sep="")
print(*[chr(ord('a') - 1 + (int(s[i] + s[i + 1]) % 26)) for i in range(len(s) - 1)], sep="")