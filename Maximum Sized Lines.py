arr = [list(map(int, input().split())) for _ in range(int(input()))]
c1, c2 = [arr[i][1] for i in range(len(arr))], [arr[i][0] for i in range(len(arr))]
arr.sort(key=lambda x: -c1.count(x[1]))
print(sum(arr[i][1] == arr[0][1] for i in range(len(arr))) - 1)
arr.sort(key=lambda x: -c2.count(x[0]))
print(sum(arr[i][0] == arr[0][0] for i in range(len(arr))) - 1)