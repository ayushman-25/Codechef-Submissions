s1, s2 = input().split(), input().split()
print("No" if any(s1[i] <= s2[len(s2) - i - 1] for i in range(len(s1))) else "Yes")
