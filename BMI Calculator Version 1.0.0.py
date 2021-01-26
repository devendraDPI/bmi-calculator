Height = float(input("Height (in Cms) : "))
Weight = float(input("weight (in Kg) : "))

# Converting Height to Meters
Height = Height/100

BMI = Weight/(Height**2)
print("Your BMI is ",BMI)

if BMI>0:
    if BMI <= 16:
        print("You are Severely Underweight")
    elif BMI <= 18.5:
        print("You are Underweight")
    elif BMI <= 25:
        print("You are Healthy")
    elif BMI <= 30:
        print("You are Overweight")
    else:
        print("You are Severely Overweight")
else:
    print("Enter Valid Details")