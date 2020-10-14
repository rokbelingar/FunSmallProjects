x = int(input("Vpišite prvo številko: "))
y = int(input("Vpišite drugo številko: "))

operation = input("Izberite matematično operacijo: ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x*y)
elif operation == "/":
    print(x/y)
