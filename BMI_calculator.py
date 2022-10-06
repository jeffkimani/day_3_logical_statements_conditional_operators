# An upgraded version of BMI calculator using conditional statements
# Accept user input
user_weight = float(input("What is your weight (kgs): "))
user_height = float(input("What is your height (m): "))

# BMI Calculation
BMI = user_weight/user_height ** 2

if BMI < 18.5:
    print(f"Your BMI is {BMI}. You are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}. You have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}. You are overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}. You are obese.")
else:
    print(f"Your BMI is {BMI}. You are clinically obese.")