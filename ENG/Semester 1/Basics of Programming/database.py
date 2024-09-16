import csv
from pathlib import Path
from prettytable import PrettyTable
#PrettyTable requires an installation! Use:
#python -m pip install -U git+https://github.com/jazzband/prettytable
#To install -> otherwise code leaves error ModuleNotFoundError: No module named 'prettytable'

path=Path('students.csv')
allStudents=[]
table=PrettyTable()
menu=['Main Menu','(1) Show Students','(2) Add Student','(3) Remove Student','(4) Import CSV','(5) Export CSV','(6) Exit']

def showStudents():
    print("Showing students...")
    table.clear()
    table.field_names=["Album","Name","Surname"]
    for i in range(len(allStudents)):
        table.add_row(allStudents[i])
    print(table)
    run() 

def addStudent():
    a = input('Album number: ')
    n = input('Name: ')
    s = input('Surname: ')
    _addStudent(a,n,s)
    run()

def _addStudent(album,name,surname):
    allStudents.append([album,name.capitalize(),surname.capitalize()])
    print(f"Student {name.capitalize()} {surname.capitalize()} ({album}) was added.")


def removeStudent():
    print("\nRemoving Student...")
    album = input('Which student do you wish to delete? Album: ')
    _removeStudent(album)

def _removeStudent(album):
    a = album
    for i in range(len(allStudents)):
        if allStudents[i][0]==a:
            temp=allStudents[i]
            allStudents.pop(i)
            print(f"Student {temp[1].capitalize()} {temp[2].capitalize()} ({temp[0]}) was removed")
    run()

def exportCSV(path):
    data=[]
    headers=f'album,name,surname'
    data.append(headers)
    for i in range(len(allStudents)):
        add=f'{allStudents[i][0]},{allStudents[i][1]},{allStudents[i][2]}'
        data.append(add)

    with open(path, 'w') as file:
        for line in data:
            file.write(f'{line}\n')
    print(f'File exported as {path}.')
    run()

def importCSV():
    if path.is_file()==True:
        allStudents.clear()
        _importCSV(path,allStudents)
    else:
        print("File students.csv doesn't exist. Please export file first.")
    run()

def _importCSV(path,og):
    new_records=[]
    i=0
    with open(path, 'r') as file:
        reader=csv.reader(file, delimiter=',')
        for row in reader:
            if reader.line_num==1:
                continue
            new_records=row
            og.append([new_records[0],new_records[1].capitalize(),new_records[2].capitalize()])
            i+=1
    if i==1:
        print('Added 1 student to database')
    else:    
        print(f'Added {i} students to database.')

def exit():
    return 0

def mainmenu():
    for i in range(len(menu)):
        if i==0:
            print('\n'+menu[i])
        else:
            print('   '+menu[i])
def goTo():
    opt = input('Go to: ')
    _goTo(opt)

def _goTo(option):
    if option=='1':
        return showStudents()
    elif option=='2':
        return addStudent()
    elif option=='3':
        return removeStudent()
    elif option=='4':
        return importCSV()
    elif option=='5':
        return exportCSV(path)
    elif option=='6':
        return exit()
    else:
        print("\nInvalid option, try again.")
        run()

def run():
    mainmenu()
    goTo()

if __name__ == '__main__':
    run()