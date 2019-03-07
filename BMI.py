#BMI Calculator in Python!
Name = "Jake"
Heightft = 6
Heightin = 1
Weight = 195
ProperBMI = 25.00
ActualHeight = (Heightft * 12) + Heightin
BMI = (Weight * 703) / (ActualHeight * ActualHeight)
print(Name, BMI)
if BMI < ProperBMI: print(Name, "is underweight")
if BMI == ProperBMI: print("Your doing great!")
else: print(Name, "is overwieght")
