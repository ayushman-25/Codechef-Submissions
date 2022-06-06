n, m = int(input()), int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
if all(sorted(set(mat[0])) == sorted(set(mat[i])) for i in range(n)):
    print("Shuffled Row Matrix")
else:
    print("Not Shuffled Row Matrix")