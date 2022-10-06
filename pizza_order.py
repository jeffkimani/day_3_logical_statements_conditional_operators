#Pizza Order Calculator
print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M, or L: ")
add_pepperoni = input("Do you want Pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
#Calculation
bill = 0
if size == "S":
    print("Small Pizza: $15")
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    print("Medium Pizza: $20")
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    print("Large Pizza: $25")
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
else:
    print("Please use the specified letters")

print(f"Your total pay will be ${bill}")