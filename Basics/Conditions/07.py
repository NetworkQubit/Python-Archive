




x = int(input("Enter Your First Number: "))
y = int(input("Enter Your Second Number: "))
z = int(input("Enter Your Choice(1. Addition 2. Subtraction 3. Multiplication 4. Division): "))

if z == 1:
    a = x + y
    print("Addition:",a)
elif z == 2:
    a = x - y
    print("Subtraction:",a)
elif z == 3:
     a = x * y
     print("Multiplication:",a)
else:
    a = x / y
    print("Division:",a)


