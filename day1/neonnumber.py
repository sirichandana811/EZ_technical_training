def is_neon_number(n):
    sq = n** 2
    s = 0
    while s!= 0:
        s= s + sq % 10
        sq = sq // 10
    return s== n

print("Neon Numbers from 0 to 100:")
for i in range(101):
    if is_neon_number(i):
        print(i)
