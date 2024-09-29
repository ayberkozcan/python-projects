import os
import sys
import time

def edit(selection):
    edit = input("Enter the task...\n")
    task[selection-1] = edit

def remove(selection):
    task.remove(task[selection-1])

def error_selection(selection):
    while True:
        try:    
            selection = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid entry. Please enter a number")
    return selection

def display(task):
    print("\nYour Tasks")
    
    if len(task) == 0:
        print("You don't have any task!\n")    
    else:
        print("---------------------------------")
        i = 0
        while i < len(task):
            print(" * " + str(task[i]))
            i = i + 1
        print("---------------------------------")

menu_inside_select = 0
task = []
i = 0
usage_index = 0

print("TO DO APP\n")

time.sleep(1)

print("Loading...\n")

time.sleep(2)

try:
    with open("todoappnogui.txt", "x"):
        pass
except FileExistsError:
    print("...\n")

with open("todoappnogui.txt","r") as file:
    task = file.readlines()

while menu_inside_select != 4:
        
    os.system('cls')
        
    display(task)
        
    time.sleep(1)
        
    print("(1) Add new task")
    print("(2) Edit task")
    print("(3) Remove task")
    print("(4) Quit")
    
    menu_inside_select = error_selection(menu_inside_select)
    
    if menu_inside_select == 1:
        add = input("Enter the task: ")
        task.append(add)
        
    elif menu_inside_select == 2:
        
        if len(task) == 0:
            print("You don't have any task!")
            break
        
        print("Select the task you want to edit")
        
        while True:
            
            menu_inside_select = error_selection(menu_inside_select)
            
            if menu_inside_select <= len(task):
                edit(menu_inside_select)
                break
            else:
                print("Try again")
        
    elif menu_inside_select == 3:
        
        if len(task) == 0:
            print("You don't have any task!")
            break
        
        print("Select the task you want to delete")
    
        while True:                
            menu_inside_select = error_selection(menu_inside_select)
            
            if menu_inside_select <= len(task):
                remove(menu_inside_select)
                break
            else:
                print("Try again")
        
    elif menu_inside_select == 4:
        
        print("See you later!!!")
        time.sleep(2)
        
        with open("todoappnogui.txt","w") as file:
            i = 0
            while i < len(task):
                file.write(task[i].rstrip() + "\n")
                i = i + 1
        
        sys.exit()
    
    else:
        print("Try again")