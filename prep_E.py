import mysql.connector

# Connessione al DB 'Animali'
mydb = mysql.connector.connect(
    host = "localhost",
    user = "pythonuser",
    password = "password123",
    database = "Animali"
)

# Creo il cursore
mycursor = mydb.cursor()

# Per il punto F eseguo la quesry per selezionare solo gli animali con peso > 2
mycursor.execute("SELECT * FROM Mammiferi WHERE Peso > 2")

# A questo punto prendo i risultati
risultati = mycursor.fetchall()

# Infine stampo i risultati con ciclo for 
for row in risultati:
    print(f"Id: {row[0]}")
    print(f"Nome_Proprio: {row[1]}")
    print(f"Razza: {row[2]}")
    print(f"Peso: {row[3]} kg")
    print(f"Età: {row[4]} anni")