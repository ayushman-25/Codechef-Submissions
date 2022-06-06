from math import ceil
ht, cud, msd = float(input()), float(input()), float(input())
cdd, cus, cds = float(input()), float(input()), float(input())
mss, cuts, cdts = float(input()), float(input()), float(input())
tt = (ht / cdts) + (cud / cus) + (cdd / cds) + 2 * (msd / mss) + (cdd / cus) + (cud / cds) + (ht / cuts)
print(ceil(tt) // 60, ceil(tt) % 60)
