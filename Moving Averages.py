arr = [int(input()) for _ in range(int(input()))]
print(format(sum([sum(arr[j] for j in range(0, i)) / i for i in range(1, len(arr) + 1)]) / len(arr), '.2f'))
