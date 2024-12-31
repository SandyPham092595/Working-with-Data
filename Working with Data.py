# Working with Data

# 1. List Comprehensions:
# Create a list of numbers from 1to 10,then use a list comprehension to create another list oftheir squares.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [number ** 2 for number in numbers]
print(squares)

# 2. Conditional Logic:
# Write a Python program that checks if a number is odd or even and prints a message based on the result.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# 3. Pizza Toppings Program:
# Write a program that asks the user for their favorite pizza toppings, append each topping to a list and print all the toppings they entered with a for loop.
toppings = []
while True:
    topping = input("Welcome to the pizzeria! What topping(s) would you like?: ")
    toppings.append(topping)
    more = input("Do you want to add more toppings? (yes/no): ")
    if more == "no":
        break  
for topping in toppings:
    print(topping)
print("Thank you for your pizza order, it'll deliver in 30 minutes!")

# https://github.com/SandyPham092595/Working-with-Data.git