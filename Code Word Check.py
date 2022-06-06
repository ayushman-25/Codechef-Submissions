a = [input() for _ in range(int(input()))]
w = input()
print("Valid" if "".join([w[int(input()) - 1] for _ in range(4)]) in a else "Invalid")