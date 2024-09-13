import sys

def display(dictionary):
    for key, value in dictionary.items():
        print(key, ":", value)

check = True

dictionary = {"apple": "elma", "water": "su", "car": "araba"}

print("--- PRIVATE DICTIONARY ---\n")

while True:
        
    display(dictionary)
    
    print("\n(1) Add")
    print("(2) Edit")
    print("(3) Remove")
    print("(4) Quit\n")
    
    select = input("Select an option... ")
    
    if select == "1":
        print("q to return")
        while True:
        
            add_key = input("Enter the key: ")
            
            if add_key == "q":
                break
            
            elif add_key in dictionary:
                print("This word already exists")
                
            else:
                add_value = input("Enter the value: ")     
                dictionary[add_key] = add_value
                break
            
    elif select == "2":
        print("q to return")
        while True:
                
            if len(dictionary) == 0:
                print("Word not found...")
                break
            
            select_edit = input("Which word do you want to edit? ")
            
            if select_edit == "q":
                break
            
            elif select_edit not in dictionary:
                print("There is no word like ", select_edit)
            
            else:
                change_edit = input("Enter the value...")
                dictionary[select_edit] = change_edit
                break
        
    elif select == "3":
        print("q to return")
        while True:
                
            if len(dictionary) == 0:
                print("Word not found...")
                break
            
            select_edit = input("Which word do you want to remove? ")
            
            if select_edit == "q":
                break
            
            elif select_edit not in dictionary:
                print("There is no word like ", select_edit)
            
            else:
                del dictionary[select_edit]
                break
        
    elif select == "4":
        sys.exit()
        
    else:
        print("Try again!\n")