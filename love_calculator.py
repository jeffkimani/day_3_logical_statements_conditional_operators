# A program that calculates love percentage by using names
#name input
print("Welcome to the Love Calculator")
first_person_name = input("Enter her name: \n")
second_person_name = input("Enter his name: \n")
#love calculation
combined_string = first_person_name +  second_person_name
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t+r+u+e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l+o+v+e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <=50:
    print(f"Your love score is {love_score}, you are alright together")
else:
    print(f"Your love score is {love_score}")