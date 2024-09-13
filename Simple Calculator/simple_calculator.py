import time
import os
import sys

def collect(x, y):
    return x + y

def ext(x, y):
    return x - y

def imp(x, y):
    return x * y

def div(x, y):
    return x / y

def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lstrip('-').isdigit():
            return int(user_input)
        else:
            print("Invalid input, please enter a valid number.")

print("Welcome To The Calculator")

time.sleep(2)

os.system('cls')

select_start = 0
begin_select = 0
select = 0

while select_start == 0:
    print("Press a to continue... ")
    begin = input()

    if begin == "a":
        while select != 5:
            print("************************")
            print("(1) Collection")
            print("(2) Extraction")
            print("(3) Impact")
            print("(4) Divide")
            print("(5) Quit")

            print("Choose the action...")

            user_input = input()

            if user_input.isdigit():
                select = int(user_input)
            else:
                print("Invalid input, please enter a number between 1 and 5.")
                continue

            if select == 1:
                no1 = get_number_input("Enter the first number: ")
                no2 = get_number_input("Enter the second number: ")
                result = collect(no1, no2)
                print(f"{no1} + {no2} = {result}")
                time.sleep(2)

            elif select == 2:
                no1 = get_number_input("Enter the first number: ")
                no2 = get_number_input("Enter the second number: ")
                result = ext(no1, no2)
                print(f"{no1} - {no2} = {result}")
                time.sleep(2)

            elif select == 3:
                no1 = get_number_input("Enter the first number: ")
                no2 = get_number_input("Enter the second number: ")
                result = imp(no1, no2)
                print(f"{no1} * {no2} = {result}")
                time.sleep(2)

            elif select == 4:
                no1 = get_number_input("Enter the first number: ")
                no2 = get_number_input("Enter the second number: ")
                if no2 != 0:
                    result = div(no1, no2)
                    print(f"{no1} / {no2} = {result}")
                else:
                    print("Error: Division by zero is not allowed.")
                time.sleep(2)

            elif select == 5:
                print("See you later!")
                time.sleep(2)
                sys.exit()

            else:
                print("Invalid selection, please choose a valid option.")

    else:
        continue
