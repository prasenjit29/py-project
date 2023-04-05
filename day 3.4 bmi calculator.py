print("bmi calculator")
height = float(input("enter your height in meters :"))
weight = float(input("enter your weight in kg :"))
bmi = round(weight/height**2)
print(f"your bmi is {bmi}")
if bmi < 18.5:
    print("you are underweight...\nyou should improve yourself...")
elif bmi < 25 :
    print("your weight is normal.....")
elif bmi < 30:
    print("you are overweight...")
elif bmi < 35:
    print("you are obese...")
else :
    print("you are chinically obese...")
