n = int(input())
arr1 = list(map(float, input().split()))
arr2 = list(map(float, input().split()))
del arr1[int(input()) - 1]
del arr2[int(input()) - 1]
diff = [format(abs(arr1[i] - arr2[i]), '.1f') for i in range(n - 1)]
print(*[int(i) if int(i) == i else i for i in arr1], end=' \n')
print(*[int(i) if int(i) == i else i for i in arr2], end=' \n')
if all(i == '0.0' for i in diff):
    print("Equal")
elif all(i == diff[0] for i in diff):
    print("Good")
else:
    print("Bad")
