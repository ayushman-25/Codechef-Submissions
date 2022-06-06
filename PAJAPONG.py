for _ in range(int(input())):
    chef, paja, k = map(int, input().split())
    roundd = chef + paja
    print("Paja" if (roundd // k) & 1 else "Chef")