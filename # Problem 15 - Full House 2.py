# Full House 2

A, B, C, D = [int(x) for x in input("Cards: ").split()]
a = A, B, C, D

if (A and B and C and D <= 13) and (A and B and C and D >= 1):
    rep = len(set(a))
    if rep == 2:
        print("Yes")
    else :
        print("No")
else : print("Wrong Input")