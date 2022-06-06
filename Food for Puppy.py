n, r = int(input()), float(input())
food = [n]
food.extend(food[i - 1] * (1 + r) for i in range(1, 6))
print(round(sum(food[1:]), 2))
