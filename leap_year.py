# Checking for a leap year
# Accept user input
print("Welcome to leap year checker!")
year = int(input("Which year do you want to check: "))
if year % 4 == 0:
    print(f"{year} is a leap year")
elif year % 100 > 0 and year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")