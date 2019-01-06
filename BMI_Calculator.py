from sys import argv

script, name = argv

print("Enter your height in inches.")
height = int(input("> "))

print("Enter your weight in pounds.")
weight = int(input("> "))

def bmi(height, weight):
    bodyMassIndex = (weight * 703 / (height**2))
    print(f"{name} your BMI is {bodyMassIndex}")
    return bodyMassIndex

bodyMassIndex = bmi(height,weight)

if bodyMassIndex < 18.5:
    print("You are underweight.")
elif bodyMassIndex >= 18.5 and bodyMassIndex < 24.9:
    print("You are normal weight.")
elif bodyMassIndex > 25 and bodyMassIndex <= 29.9:
    print("You are overweight.")
elif bodyMassIndex > 30:
    print("You are obesse.")
