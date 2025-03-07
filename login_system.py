import password_checker

def register(username,password,filename="credentials.txt"):
    with open(filename,'a') as file:
        file.write(f"{username}:{password}\n")
        print("registered successfully")

def login(username,password,filename="credentials.txt"):
    with open(filename,'r') as file:
        for line in file:
            print(line)
            if ':' in line:
                stored_username,stored_password = line.strip().split(':',1)
            if (stored_username == username and stored_password == password) :
                print("loged In")
            else:
                print("enter valid credentials")

option=input("new user or existing user :")
if option.lower()== 'new user':
    username=input("Username : ")
    password=input("password : ")
    password_checker.password_check(password)
    register(username,password)
    print("to continue login")
    login(username,password)
elif option.lower()=='existing user':
    username=input("Username : ")
    password=input("password : ")
    login(username,password)
else:
    print("enter valid input!")







