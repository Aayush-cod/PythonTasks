a = eval(input("Enter your marks:"))

if a > 80:
    print("A")
elif a >= 60 and a <= 80:
    print("B")
elif a >= 50 and a < 60:
    print("C")
elif a >=45 and a < 50:
    print("D")
elif a >= 25 and a < 45:
    print("E")
elif a < 25:
    print("F")
else:
    print("Fail!!")