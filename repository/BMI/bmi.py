import time

weight_unit = input("Weight in unit KG or Lbs? ")
weight = 0

while not weight:

    if weight_unit.lower() == "kg":
        while True:
            try:
                weight = int(float(input("Weight: ")))
            except ValueError:
                print("Please type your weight in numbers. ")
            else:
                break

        print(f'Your weight is {round(weight, 2)} KG')

    elif weight_unit.lower() == "lbs":
        while True:
            try:
                weight = int(float(input("Weight: ")))
            except ValueError:
                print("Please type your weight in numbers. ")
            else:
                break

        print(f'Your weight is {weight* 0.454} KG')

    else:
        weight_unit = input("Please type either of these - KG or Lbs. ")


time.sleep(1)

height_unit = input("Please ft or cms? ")
height = 0

while not height:

    if height_unit.lower() == "ft":
        while True:
            try:
                height = int(float(input("Height: ")))*0.3048
            except ValueError:
                print("Please type your height in numbers. ")
            else:
                break

        print(f"Your weight is {round(height, 2)} mtr")

    elif height_unit.lower() == "cms":
        while True:
            try:
                height = int(float(input("Height: ")))/100
            except ValueError:
                print("Please type your height in numbers. ")
            else:
                break
        print(f'Your weight is {round(height, 2)} mtr')

    else:
        height_unit = input("Please type either of these - ft or cms. ")

bmi = weight / (height*height)
time.sleep(1)
print(f'The Body Mass Index is : {bmi}.')
if 19 > bmi >= 9:
    print("Your BMI indicates that you are underweight.")
elif 24 > bmi >= 19:
    print("Your BMI indicates that you are healthy.")
elif 29 > bmi >= 25:
    print("Your BMI indicates that you are overweight.")
elif 39 > bmi >= 30:
    print("Your BMI indicates that you are obese. ")
elif 65 > bmi >= 40:
    print("You are extremely Obese. ")
else:
    print("Please run the program again and type the correct values")