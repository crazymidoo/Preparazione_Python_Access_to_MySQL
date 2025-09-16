import mysql.connector

# Connessione al DB
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
)

# Creo un cursore per eseguire i comandi SQL
mycursor = mydb.cursor()

# Creo la tabella Mammiferi 
mycursor.execute("CREATE TABLE Mammiferi (Id INT AUTO_INCREMENT PRIMARY KEY, Nome_Proprio VARCHAR(100), Razza VARCHAR(100), Peso INT, Eta INT)")
