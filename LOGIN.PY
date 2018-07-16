PASTEBINnew paste 


 Untitled
 SUEDEW     SEP 9TH, 2016  1,014   NEVER

Not a member of Pastebin yet? Sign Up, it unlocks many cool features!
rawdownloadreport 0.79 KB
#start
 
users = {}
status = ""
 
def displayMenu():
    status = input("Are you registered user? y/n? Press q to quit")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
 
def newUser():
    createLogin = input("Create login name: ")
 
    if createLogin in users:
        print("\nLogin name already exist!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\nUser created\n")
 
def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")
 
    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")
 
while status != "q":
    displayMenu()
   
#end