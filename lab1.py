import math
##problem 1.1
radius = 5
area = math.pi * radius ** 2

print(area)
##problem 1.2
radius2 = 3
volume = (4/3) * math.pi * radius2 ** 3

print(volume)
##problem 1.3
a = 3
b = 4
hypotenuse = math.sqrt(a**2 + b**2)

print(hypotenuse)
##problem 2
##create a string variable containing your full name
full_name = "Liam McSeveney"

##print the length of your name
name_length = len(full_name)
print("Length of your name:", name_length)

##concatenate your first name and last name with a space in between
first_name = "Liam"
last_name = "McSeveney"
concatenated_name = first_name + " " + last_name
print("Concatenated name:", concatenated_name)

##convert your name to uppercase and lowercase
uppercase_name = full_name.upper()
lowercase_name = full_name.lower()
print("Uppercase name:", uppercase_name)
print("Lowercase name:", lowercase_name)
##problem 3
##create variables to store your age, height (in feet), and weight (in pounds).
age = 24
height_feet = 6
weight_pounds = 195

##print the data type of each variable using the type() function.
print("Data type of age:", type(age))
print("Data type of height_feet:", type(height_feet))
print("Data type of weight_pounds:", type(weight_pounds))

##calculate your Body Mass Index (BMI)
##convert height from feet to inches
height_inches = height_feet * 12

##calculate BMI using the formula
bmi = (weight_pounds / height_inches ** 2) * 703

##print your BMI
print("Your BMI is:", bmi)