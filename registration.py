import os
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
pattern = "^.*(?=.{8,})(?=.*)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=.]).*$"


def user_check():
    if re.fullmatch(regex, username):
        print("Valid Email")
        check_pwd()
    else:
        print("Invalid Email")
        print("email/username should have @ and followed by . , eg:- nikhi@gmail.com")
        register()


def check_pwd():
    result = re.findall(pattern, password)
    if result:
        print("Valid password")
        register_user()
    else:
        print("Password not valid - Try again")
        print("password length 5- 15 and must have minimum one special character,one digit,one uppercase and lowercase character")     
        register()


def register():
    global username, password
    print("register")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    user_check()


def register_user():
    username_info = username
    password_info = password
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    print("Registration Successful")
    main()


def login():
    global username_verify, password_verify
    print("login")
    print("Enter Username: ")
    username_verify = input()
    print("Enter Password: ")
    password_verify = input()
    login_verify()


def login_verify():
    username1 = username_verify
    password1 = password_verify
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            print("Login Successful!!")
        else:
            print("Password has not been recognised")
            print("1.Retry")
            print("2.Forgot")
            print("3.Exit")

            while True:
                choice = input("Enter choice(1/2/3/): ")
                if choice in ('1', '2', '3'):
                    if choice == '1':
                        login()
                    elif choice == '2':
                        forgot()
                    elif choice == '3':
                        break
                    break
                else:
                    print("Invalid Input")
    else:
        print("User not found")
        print("Try again or Register")
        main()


def forgot():
    username_info = username_verify
    print("Username and Password is:")
    file = open(username_info, "r")
    for each in file:
        print(each)
    file.close()
    main()


def main():
    print("Select operation.")
    print("1.Login")
    print("2.Register")
    print("3.Exit")

    while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/): ")

        # Check if choice is one of the three options
        if choice in ('1', '2', '3'):
            if choice == '1':
                login()
            elif choice == '2':
                register()
            elif choice == '3':
                break
            break
        else:
            print("Invalid Input")


main()
