"""
Exercise 1:
    Basic Variables
"""

my_name = "Destine"
my_age = 21
my_favorite_programming_language = "Python"
completed_class = True
print("Name:", my_name)
print("Age:", my_age)
print("Favorite Programming Language:", my_favorite_programming_language)
print("Completed Class:", completed_class)



"""
Exercise 2: 
    Variable Operations
"""
num1 = 15
num2 = 4

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2


print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)


"""Exercise 3: 
    String Manipulation
"""
first_name = "Destine"
last_name = "Honu"
full_name = first_name + " " + last_name
full_name_upper = full_name.upper()
about_me = f"My name is {full_name} and I am {my_age} years old.\nI love programming in {my_favorite_programming_language}."
print(about_me)


"""Exercise 4:
    User Input
"""
favorite_food = input("What is your favorite food? ")
times_eaten = int(input("How many times do you eat it per week? "))
print(f"My favorite food is {favorite_food} and I eat it {times_eaten} times a week.")


"""Exercise 5:
    Type Conversion
"""
age = "25"
height = 5.8
print("I am " + age + " years old and " + str(height) + " feet tall.")


"""
Exercise 6:
    Simple Calculator
"""
temperature_celcius = float(input("Enter temperature in Celsius: "))
temperature_fahrenheit = (temperature_celcius * 9 / 5) + 32
print(f"Temperature in Celcius: {temperature_celcius}°C")
print(f"Temperature in Fahrenheit: {temperature_fahrenheit}°F")
