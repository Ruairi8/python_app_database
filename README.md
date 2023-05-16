# python_app_database
---
## Repository Contents:
- 'AppDatabases.py' python file
- 'AppDatabases2.py' python file
- 'sqlStatements.txt' text file

## Description:
- User menu using Python
- Connecting to the Neo4j graph database 
- Connecting to MySQL using a Virtual Machine (Azure labs)
- CRUD operations (create, read, update, delete)

## Requirements:
Python 3.8<br><br>
pymysql 1.0.3<br>
<br>
On command line (pip is automatically installed if using a Virtual Environment. In Python 3.4 or higher, pip in automatically built-in):
``` python
pip install pymysql
```
Or in anaconda prompt: 
``` python
conda install pymysql
```
Neo4j graph database:
``` python
pip install neo4j
```
A connection to MySQL, see [azure](https://learn.microsoft.com/en-us/azure/mysql/single-server/connect-workbench)
The MySQL workbench can be got via Azure labs or Wampserver for example.
<br>
Get MySQL server running; then run the following into you  cmder or VScode and click enter: 
```python
python appDatabases.py
```
You can then interact with the user menu.

### Download MySQL on Windows:
The default installation directory is <b>C:\Program Files\MySQL\MySQL Server 8.0</b> for installations performed with MySQL Installer. 
MySQL Installer requires Microsoft .NET Framework 4.5.2 or later.
To invoke MySQL Installer after a successful installation:<br>
Right-click Windows Start, select Run, and then click Browse. Navigate to Program Files (x86) > MySQL > MySQL Installer for Windows to open the program folder.

Select one of the following files:<br>
<b>MySQLInstaller.exe</b> to open the graphical application.<br>
<b>MySQLInstallerConsole.exe</b> to open the command-line application.

Click <b>Open</b> and then click <b>OK</b> in the Run window. If you are prompted to allow the application to make changes to the device, select Yes.

[https://dev.mysql.com/doc/refman/8.0/en/](https://dev.mysql.com/doc/refman/8.0/en/)
