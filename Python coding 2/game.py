z = (1, 2, 3, 4, 5)

x = int(input("Choose a number from z: "))
y = int(input("Choose another number from z: "))

sum = x + y

if x % 2 != 0:
    print("x is odd")
    if sum % 2 != 0:
        print("x is won")
    else:
        print("x is lost")
else:
    if sum % 2 != 1:
        print("y is won")
    else:
        print("y is lost")
