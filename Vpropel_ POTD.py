n, w, curr_match = input(), input(), 0
if(len(w) * 2 != len(n)): print(-1); exit(0)
alp = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
for i in range(0, len(n), 2):
    if(alp.index(w[curr_match]) % 52 == int(n[i] + n[i + 1]) - 1): curr_match += 1
    else: break
print(curr_match)