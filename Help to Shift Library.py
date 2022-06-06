n = int(input())
trip, ramu, somu, last = 1, 0, 0, None
while 1:
    ramu += trip << int(not(trip & 1))
    if ramu + somu >= n:
        ramu -= ramu + somu - n
        last = "Ramu"
        break
    somu += trip << (trip & 1)
    if ramu + somu >= n:
        somu -= ramu + somu - n
        last = "Somu"
        break
    trip += 1
print(str(trip) + "\n" + str(ramu) + "\t" + str(somu) + "\n" + str(last))
