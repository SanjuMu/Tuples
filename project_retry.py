tup1= (4, 3, 2, 2, -1, 18)
tup2= (2, 4, 8, 8, 3, 2, 9)

multi= 1
multi2= 1

for num in tup1:
    multi *= num

for num in tup2:
    multi2 *= num

print("The product of tup1 is",multi)
print("The product of tup2 is",multi2)