import pyodbc 

# server = 'kms-db.database.windows.net'
# database = 'kms_dev'
# username = 'kmsadmin@kms-db'
# password = 'Dotvik@98765'
# driver= '{SQL Server}'
# connectionString = 'DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password

cs = (
    "DRIVER={SQL Server};"
    "SERVER=kms-db.database.windows.net;"
    "UID=kmsadmin@kms-db;"
    "database=kms_dev;"
    "PWD=Dotvik@98765;"
    )
print(cs)
cnxn = pyodbc.connect(cs)
print("Connected.")
# cnxn.close()

# print(connectionString)
# cnxn = pyodbc.connect(connectionString)

# https://stackoverflow.com/questions/32662123/pyodbc-error-data-source-name-not-found-and-no-default-driver-specified-paradox