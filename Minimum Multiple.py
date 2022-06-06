arr, m = sorted([int(input()) for _ in range(int(input()))]), int(input())
arr.sort(key=lambda x: [x % m])
print(arr[0] if not(arr[0] % m) else "No multiple found")