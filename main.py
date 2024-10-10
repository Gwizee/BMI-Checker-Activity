height = float(input("Enter your heigth in CM :" ))
weight = float(input("Enter you weight in KG :" ))

BMI = weight / ((height/100)**2)
print("Your BMI is ",BMI)
if BMI <= 18.5 :
    print("You are Under Weight")
elif BMI <= 24.9 :
    print("You are Healthy")
elif BMI <= 29.9 :
    print("You are Over Weight")
elif BMI <= 34.9 :
    print("You are Severely Over Weight")
elif BMI <= 39.9 :
    print("Your are obese")
else :
    print("You are Severely Obese")