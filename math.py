# name = "Jon"
# age = 30
# actual_age = 31.11 ## float

# print(name)
# print(age)

# to print the data type of the variable
# print(type(name))
# print(type(age))
# print(type(actual_age))

# math = 30 + 5 * 45 / 24 ** 100
# results = age + actual_age + math

# print(results)


# Take user input and store it in variable name
name = input("What is your name?\n")

print("Hello " + name + ", thank you for coming today\n")

# put a string into a variable
menu = "Black Coffee, Espresso, Latte, Cappuccino"

# print out the variable string menu
print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")

# get user input and store it in variable order
order = input()
price = 8
quantity = input("How many cups of coffee would you like?\n")
# convert quantity from a string to an integer
total = price * int(quantity)

# print out the the customer's name, and show you your order
print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment. Your total bill is: $" + str(total))

