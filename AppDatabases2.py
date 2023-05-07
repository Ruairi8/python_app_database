# pymysql package required installation from pip:
import pymysql


def connect():
    global conn
    conn=pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor)
	
def function():
    if (not conn):
        print("NO connection!!")
        connect()
		
def choice1():
    conn=pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor)
    with conn:
        cursor = conn.cursor()
        query = "SELECT DISTINCT a.name AS N1, b.name AS N2 FROM employee a JOIN dept b ON a.did = b.did ORDER BY b.name;"
        cursor.execute(query)
        rows = cursor.fetchmany(size=2)
        for row in rows:
            print(row["N1"] + " | " + row["N2"])


def choice2():
    conn=pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor)
    with conn:
        cursor = conn.cursor()
        query = "SELECT DISTINCT a.name AS N1, b.name AS N2 FROM employee a JOIN dept b ON a.did = b.did ORDER BY b.name;"
        cursor.execute(query)
        x = cursor.fetchall()
        for i in range(0, len(x), 2):
            for row in x[i:i+2]:
                print(row["N1"] + " | " + row["N2"]) 
            if input("-- Quit (q) --") == "q":
                break
        print("-- Quit (q) --")

def empID():
    conn=pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor)
    with conn:
        cursor = conn.cursor()
        eid = input("Enter EID: ")
        if (checkID(eid) == True):
            print("Salary Details For Employee: {}".format(eid))
            data = (eid,)
            query = "SELECT a.eid, MIN(FORMAT(b.salary, 2)) AS S, FORMAT(AVG(b.salary), 2) AS U, MAX(FORMAT(b.salary, 2)) AS V FROM employee a JOIN salary b ON b.eid = a.eid WHERE a.eid=%s;"
            cursor.execute(query, data)
            x = cursor.fetchall()
            for id in x:
                print("-----------------------------")
                print("Minimum  " + "  |  " + "Average  " + "  |  " + "Maximum")
                print(id["S"]  + "  |  " +  id["U"]  + "  |  " + id["V"])
        else:
            print("------------------------")
            print("Minimum  |  Average  |  Maxiumum")
        
def checkID(eid):
    conn=pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor)
    query = "SELECT * FROM employee WHERE eid=%s"
    c = conn.cursor()
    x = (eid,)
    c.execute(query,x)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def month():
    conn=pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor)
    with conn:
        cursor = conn.cursor()
        a = input("Enter Month: ")
        data = (a,)
        query = "SELECT eid, name, dob FROM employee WHERE LEFT(MONTHNAME(dob),3)=%s;"
        cursor.execute(query,data)
        x = cursor.fetchall()
        for month in x:
            print((str(month["eid"])) + " | " + str(month["name"])) + " | " + str((month["dob"]))
        

def newEmp():
    conn=pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor)
    with conn:
        try:
            cursor = conn.cursor()
            print("Add New Employee")
            print("----------------")
            eid = input("EID : ")
            Name = input("Name :")
            DOB = input("DOB :")
            DepID = input("Dept ID :")
            data = (eid, Name, DOB, DepID)
            if (checkID(eid)==False):
                query = "INSERT INTO employee VALUES(%s,%s,%s,%s)"
                cursor = conn.cursor()
                cursor.execute(query,data)
                conn.commit()
                print("Employee successfully added")
            else:
                print("*** ERROR ***: {} already exists".format(eid))
        except pymysql.err.OperationalError:
            print("*** ERROR ***: Invalid DOB: {}".format(DOB))
        except pymysql.err.IntegrityError:
            print("*** ERROR ***: Department {} does not exist".format(DepID))

def checkDate(dob):
    conn=pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor)
    query = "SELECT * FROM employee WHERE dob=%s"
    c = conn.cursor()
    x = (dob,)
    c.execute(query,x)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def viewDept():
    conn=pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor)
    with conn:
        cursor = conn.cursor()
        a = input("Enter EID : ")
        print("Departments managed by {}".format(a))
        print("-------------------------")
        if (checkID(a)==True):
            data = (a,)
            query = "SELECT a.did AS did, FORMAT(a.budget, 0) AS Budget FROM dept a JOIN employee b ON b.did = a.did WHERE b.eid=%s;"
            cursor.execute(query,data)
            x = cursor.fetchall()
            for y in x:
                print("Department   |   Budget") 
                print(y["did"]  + " | " +  str(y["Budget"]))
        else:
            print("Department   |   Budget")

# neo4j package required installation from pip: "Successfully installed neo4j-5.8.0"
from neo4j import GraphDatabase

driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "neo4j"), max_connection_lifetime=1000)

def func(tx, i, d):
    query = "CREATE(a:Employee{eid:$id}) CREATE(b:Department{did:$dept}) CREATE(a)-[:MANAGES]->(b)"
    tx.run(query, id=i, dept=d)

def func2(tx, d):
    query = "MATCH(a:Employee)-[:MANAGES]->(b:Department{did:$dept})"
    tx.run(query, dept=d)

def manager():
    connect()
    id = input("Enter EID : ")
    dept = input("Enter DID : ")
    if (checkID(id)==True) and (checkDept(dept)==True):
        with driver.session() as session:
            values = session.write_transaction(func, id, dept)
            print("Employee {} now manages department {}".format(id, dept))
            return values
    elif (func2==True):
        print("Department {} is already run by {}".format(dept, id))
    else:
        print("Employee {} does not exist".format(id))
        print("Department {} does not exist".format(dept))
        manager()

def checkDept(did):
    conn=pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor)
    query = "SELECT * FROM dept WHERE did=%s"
    c = conn.cursor()
    x = (did,)
    c.execute(query,x)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def viewAll():
    conn=pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor)
    with conn:
        cursor = conn.cursor()
        query = "SELECT * FROM dept"
        cursor.execute(query)
        x = cursor.fetchall()
        for data in x:
            print(data["did"] + " | " + data["name"] + " | " + data["lid"] + " | " + data["budget"])
            cursor.close()