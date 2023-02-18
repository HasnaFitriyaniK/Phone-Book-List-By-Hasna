import os
import json
import re

name = input ("What's ur name?\n")
os.system('cls')

print("Hi", name.upper(), "\nWelcome to Phone Book 2023 with Python by Hasna\n")
print("Here are the list number of people in ur neighborhood")
file = open("PhoneBookList.txt", "r")
print(file.read())
file.close()
print("What do u want to do?")

def menu():
    print("1. Create\n2. Read\n3. Update\n4. Delete")
    acts = int(input("\nChoose the action:"))
    return acts

def create():
    print("\nYou want to create new contact.")
    name = input("Name (Spasi) Number: ")
    file = open ("PhoneBookList.txt", "a")
    file.write("\n")
    file.write(name)
    file.close()

#def read():
    #file = open("PhoneBookList.txt", "r")
    #print(file.read())
    #file.close()

def update():
    updnamnum = input("What do u want to update/change?\n1. Name\n2. Number\n3. Go Back\nI choose: ")
    if updnamnum == "1":
        file2 = open("PhoneBookList.txt", "r")
        old_name = input("Enter old name: ")
        new_name = input("Enter new name: ")
        s = re.sub(old_name, new_name, file2.read())
        file = open("PhoneBookList.txt", "w")
        file.writelines(s)
        file2.close()
        file.close()
    elif updnamnum == "2":
        file2 = open("PhoneBookList.txt", "r")
        old_number = input("Enter old number: ")
        new_number = input("Enter new number: ")
        s = re.sub(old_number, new_number, file2.read())
        file = open("PhoneBookList.txt", "w")
        file.writelines(s)
        file2.close()
        file.close()
    elif updnamnum == "3":
        menu()
    else:
        print("It's a wrong input!!")
        input()
        
    
def read():
    with open("PhoneBookList.txt", "r") as data_file:
        for line in data_file:
            data = line.split()
            print(data)

def delete():
    string_to_delete = input("Enter the name to delete: ")
    with open("PhoneBookList.txt", "r") as f:
        lines = f.readlines()

    with open("PhoneBookList.txt", "w") as f:
        for line in lines:
             if string_to_delete.lower() not in line.lower():
                f.write(line)
     
while True :
    acts = menu()
    match acts:
        case 1:
            create()
        case 2:
            read()
        case 3:
            update()
        case 4:
            delete()
