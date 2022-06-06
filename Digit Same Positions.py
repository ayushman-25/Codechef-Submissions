n1, n2, fnd = input()[::-1], input()[::-1], False
ans = ["Same at " + ("1's" if not i else str(10 ** i) + "th") + " position" for i in range(len(n1)) if n1[i] == n2[i]]
print("No digits are same" if not ans else "\n".join(ans))
