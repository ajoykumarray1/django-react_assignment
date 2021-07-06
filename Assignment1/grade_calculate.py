n = float(input("Enter Grade: "))
if n == 4:
    print("A+")
elif n >= 3.75 and n <= 3.99:
    print("A")
elif n >= 3.26 and n <= 3.74:
    print("A-")
elif n >= 3.1 and n <= 3.25:
    print("B+")
elif n >= 2.76 and n <= 3:
    print("B")
elif n >= 2.51 and n <=2.75:
    print("B-")
elif n >= 2.1 and n <= 2.5:
    print("C")
elif n == 2:
    print("D")
elif n<2:
    print("Fail")
else:
    print("Invalid")
