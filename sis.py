import re
import sys

main_list = []
studentList = []
email_validators = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def mainList():
    print(main_list)

#To Display the list
def displayList():
    print(studentList)
    mainList()

#To add items to the list
def appendList(x):
    studentList.append(x)
    displayList()

#function to make all inputs mandatory
def mandatory(x):
    if len(x) == 0:
        x = input("Cannot be Empty::\n")
        mandatory(x)
    else:
        appendList(x)

#Function to check if the len of mobNo and prn
def check_len(x):
    if len(x)!=10:
        x = input("Enter Again\nShould be of 10 digits:\n")
        check_len(x)
    else:
        appendList(x)
        

#function to validate a email
def validate_email(email):  
    if(re.search(email_validators,email)):  
        appendList(email) 
          
    else:  
        email = input("Enter a valid Email\n")  

def saveData():
    with open("sis.txt", "w") as sis:
        sis.write("\n".join(str(item) for item in main_list))

def deleteData():
    print("Delete Data!")

def inputData():
    rollNo = input("Enter your Roll No:\n")
    mandatory(rollNo)

    prn = input("Enter Your PRN:\n")
    check_len(prn)

    name = input("Enter your name:\n")
    mandatory(name)

    mobNo = input("Enter your Mobile Number:\n")
    check_len(mobNo)

    email = input("Enter your email Id:\n")
    validate_email(email)

    city = input("Enter your City!:\n")
    mandatory(city)
    state = input("Enter your state:\n")
    mandatory(state)

    main_list.append(studentList)
    


  
x = int(input("Press 0 to exit \n 1: Add Records\n 2: Save Records \n 3: Delete Records\n"))
while x!=0:
    if x == 1:
        inputData()
    elif x == 2:
        saveData()
    elif x == 3:
        deleteData()
    if x == 0:
        main()
        sys.exit()
    x = int(input("Press 0 to exit \n 1: Add Records\n 2: Save Records \n 3: Delete Records\n"))

    