weight=float(input('enter weight in kg:'))
height=float(input('enter height in meter:'))

bmi=weight/height**2

##print((bmi))

if bmi <18.5:
    print("your BMI is {bmi} and you are underweight")
elif bmi <25:
    print("your BMI is {bmi} and you have a normalweight")
elif bmi <30:
    print("your BMI is {bmi} and you are overweight")
elif bmi <35:
    print("your BMI is {bmi} and you are Obes")
else:
    print("your BMI is {bmi} and you are clinically Obese")
    
     
