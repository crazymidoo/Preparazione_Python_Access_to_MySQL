import mysql.connector

# Connessione al DB 'Animali' già creato
mydb = mysql.connector.connect(
    host = "localhost",
    user = "pythonuser",
    password = "password123",
    database = "Animali"
)

mycursor = mydb.cursor()

# Seleziono tutti gli animali dalla tabella Mammiferi
mycursor.execute("SELECT * FROM Mammiferi")

# Recupero tutti i risultati
risultati = mycursor.fetchall()

# Stampo i dati utilizzando il ciclo for
for row in risultati:
    print(f"Id: {row[0]}")
    print(f"Nome_Proprio: {row[1]}")
    print(f"Razza: {row[2]}")
    print(f"Peso: {row[3]}")
    print(f"Età: {row[4]}")
