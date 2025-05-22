import pyodbc
server = 'xxx.xxx.xxx.xxx' 
database = 'CompanyDB'
username = 'YourUsername'
password = 'YourPassword123'

connection_string = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password}"
)

try:
    connection = pyodbc.connect(connection_string)
    print("Connection to SQL Server successful.")

    cursor = connection.cursor()

    query = "SELECT TOP 5 * FROM Employees"

    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

except pyodbc.Error as e:
    print("Error occurred while connecting to the database ")
    print(e)

finally:
    if 'connection' in locals():
        connection.close()
        print("Connection closed.")