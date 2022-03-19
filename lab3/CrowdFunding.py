import re
from getpass import getpass
import json


def LoadClientsData():
    try:
        with open("ClientsData.json", "r") as readJson:
            clientsData = json.load(readJson)
    except:
        clientsData = []
    finally:
        return clientsData


clientsData = LoadClientsData()
currentClientIndex = -1


def CheckAlNum(newStr):
    regex = r'\b[A-Za-z0-9 ]+\b'
    if re.fullmatch(regex, newStr):
        return True
    return False


def CheckNum(newStr):
    if newStr.isdigit():
        return True
    return False


def CheckDate(date):
    regex = r'\b([0-9]{2}-){2}[0-9]{4}\b'
    if re.fullmatch(regex, date):
        day, month, year = date.split("-")
        if int(day) <= 31 and int(month) <= 12 and int(year) >= 2022:
            return True
    return False


def GetProjectDate():
    sdate = input("Enter start date (dd-mm-yyyy): ")
    while CheckDate(sdate) == False:
        sdate = input("Invalid date try again: ")
    edate = input("Enter end date (dd-mm-yyyy): ")
    while CheckDate(edate) == False:
        edate = input("Invalid date try again: ")
    return sdate, edate


def GetProjectTarget():
    target = input("Enter Project Target: ")
    while CheckNum(target) == False:
        target = input("Target must be a positive integer try again: ")
    return target


def GetProjectDetails():
    details = input("Enter project details: ")
    while CheckAlNum(details) == False:
        details = input("Details should be alphanumeric try again: ")

    return details


def CheckTitleExists(title):
    projectIndex = -1
    for project in clientsData[currentClientIndex].get("projects"):
        projectIndex += 1
        if project.get("title") == title:
            return projectIndex
    return -1


def GetProjectTitle():
    title = input("Enter Project Title: ")
    while CheckAlNum(title) == False:
        title = input("Title should be alphanumeric try again: ")

    while CheckTitleExists(title) != -1:
        title = input("Project with same title already exists try again: ")

    return title


def GetProjectInfo():
    title = GetProjectTitle()
    details = GetProjectDetails()
    target = GetProjectTarget()
    sdate, edate = GetProjectDate()
    projectInfo = {"title": title, "details": details,
                   "target": target, "sdate": sdate, "edate": edate}
    return projectInfo


def CreateProject():
    projectInfo = GetProjectInfo()
    global clientsData
    clientsData[currentClientIndex].get("projects").append(projectInfo)
    WriteToJson()
    print("Project successfully created")


def ViewProjects():
    if len(clientsData[currentClientIndex].get("projects")) == 0:
        print("You currently have no projects")
    else:
        for project in clientsData[currentClientIndex].get("projects"):
            print(project)


def EditProject():
    title = input("Enter Project Title: ")
    projectIndex = CheckTitleExists(title)
    if projectIndex == -1:
        print("No project exists with same title")
    else:
        newProjectInfo = GetProjectInfo()
        clientsData[currentClientIndex].get(
            "projects")[projectIndex] = newProjectInfo
        WriteToJson()
        print("Project successfully Edited")
    pass


def DeleteProject():
    title = input("Enter Project Title: ")
    projectIndex = CheckTitleExists(title)
    if projectIndex == -1:
        print("No project exists with same title")
    else:
        project = clientsData[currentClientIndex].get("projects")[projectIndex]
        clientsData[currentClientIndex].get("projects").remove(project)
        WriteToJson()
        print("Project successfully Deleted")


def ProjectsMenu():
    while True:
        print("1- Create Project\n2- View Projects\n3- Edit Project\n4- Delete Project\n5- Main Menu")
        userInput = input("Enter your choice: ")
        if userInput == '1':
            CreateProject()

        elif userInput == '2':
            ViewProjects()

        elif userInput == '3':
            EditProject()

        elif userInput == '4':
            DeleteProject()

        elif userInput == '5':
            break


def WriteToJson():
    with open("ClientsData.json", "w") as writeJson:
        json.dump(clientsData, writeJson)


def CheckMailExists(mail):
    for account in clientsData:
        if account.get("mail") == mail:
            return True
    return False


def CheckLogin(mail, password):
    clientIndex = -1
    for account in clientsData:
        clientIndex += 1
        if account.get("mail") == mail and account.get("password") == password:
            return clientIndex

    return -1


def CheckClientPhone(phone):
    regex = r'01[0125][0-9]{8}'
    if re.fullmatch(regex, phone):
        return True
    return False


def GetClientPhone():
    phone = input("Enter your phone number: ")
    while CheckClientPhone(phone) == False:
        phone = input("Invalid Phone numer try again: ")
    return phone


def GetClientPassword(isRegistering):

    while True:
        password = getpass("Enter your password(hidden): ")
        if isRegistering:
            repassword = getpass("Retype your password(hidden): ")
            if password != repassword:
                print("Passwords don't match try again")
            else:
                break
        else:
            break
    return password


def CheckClientMail(mail):
    regex = r'([A-za-z0-9].?)+@[A-Za-z]+\.(com|org)'
    if re.fullmatch(regex, mail):
        return True
    return False


def GetClientMail(isRegistering):
    mail = input("Enter your mail: ")
    while CheckClientMail(mail) == False:
        mail = input("Invalid mail try again: ")
    if isRegistering:
        while CheckMailExists(mail):
            mail = input("Same mail already exists try again: ")
    return mail


def CheckAlpha(name):
    if (name.isalpha()):
        return True
    return False


def GetClientName():
    fname = input("Enter first name: ")
    while CheckAlpha(fname) == False:
        fname = input("Invalid name try again: ")
    lname = input("Enter last name: ")
    while CheckAlpha(lname) == False:
        lname = input("Invalid name try again: ")
    return fname, lname


def Register():
    fname, lname = GetClientName()
    mail = GetClientMail(True)
    password = GetClientPassword(True)
    phone = GetClientPhone()
    projects = []
    clientInfo = {"fname": fname, "lname": lname, "mail": mail,
                  "password": password, "phone": phone, "projects": projects}

    global clientsData
    clientsData.append(clientInfo)
    WriteToJson()
    print("Successfully Registered")


def Login():
    mail = GetClientMail(False)
    password = GetClientPassword(False)
    clientIndex = CheckLogin(mail, password)
    if clientIndex == -1:
        print("Login failed invalid credentials")

    else:
        global currentClientIndex
        currentClientIndex = clientIndex
        print("Successfully Logged In")
        ProjectsMenu()


def MainMenu():
    while True:
        print("1- Login\n2- Register\n3- Exit")
        userInput = input("Enter your choice: ")
        if userInput == '1':
            Login()
        elif userInput == '2':
            Register()
        elif userInput == '3':
            break


MainMenu()
