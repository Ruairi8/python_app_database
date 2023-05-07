# Python app for Applied Databases
import AppDatabases2
import pymysql

conn = None
def connect():
    global conn
    conn = pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor)

def choice1():
    query = "SELECT Employee Name, Department Name FROM employees"
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchmany(size=2)
        for row in rows:
            print(row["Employee Name"] + " | " + row["Department Name"])
#       conn.close()

def menu():
    print("Employees")
    print("---------\n\n")
    print("MENU\n")
    print("====")
    print("1 - View Employess & Departments")
    print("2 - View Salary Details")
    print("3 - View by Month of Birth")
    print("4 - Add New Employee")
    print("5 - View Departments managed by Employee")
    print("6 - Add Manager to Department")
    print("7 - View Deparments")
    print("x - Exit Application")
    choice()

def choice():
    while True:
        a = input("Choice: ")
        if a == 1:
            AppDatabases2.choice2()
            menu()
        elif a == 2:
            AppDatabases2.empID()
        elif a == 3:
            AppDatabases2.month()
        elif a == 4:
            AppDatabases2.newEmp()
        elif a == 5:
            AppDatabases2.viewDept() 
        elif a == 6:
            pass
        elif a == 7:
            pass
        elif a == "x":
            pass

            
if __name__ == "__main__":
    menu()