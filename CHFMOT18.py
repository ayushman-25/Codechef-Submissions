for _ in range(int(input())):
    price_to_be_paid, n = map(int, input().split())
    coins = 0
    if(price_to_be_paid // n == (price_to_be_paid / n)):
        print(price_to_be_paid // n)
    else:
        coins = 0
        coins += (price_to_be_paid // n)
        price_to_be_paid %= n
        if(price_to_be_paid % 2 == 0) or (price_to_be_paid == 1):
            coins += 1
        else:
            coins += 2
        print(coins)s