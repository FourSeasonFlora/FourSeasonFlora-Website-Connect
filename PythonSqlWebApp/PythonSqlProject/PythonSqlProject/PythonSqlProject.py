import pyodbc

server = '' 
database = '' 
username = '' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';'+'Trusted_Connection=yes')
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM blog")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()