import mysql.connector

# Connessione al DB 'Animali'
mydb = mysql.connector.connect(
    host="localhost",
    user="pythonuser",
    password="password123",
    database="Animali"
)

mycursor = mydb.cursor()

# Inserisco un record nella tabella Mammiferi (scrivo la query con i valori direttamente)
mycursor.execute("INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES ('Ghito', 'Gatto', 4, 2)")

# La consegna ne chiede 5 quindi:
mycursor.execute("INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES ('Kiko', 'Cane', 25, 3)")
mycursor.execute("INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES ('Zizo', 'Zebra', 180, 6)")
mycursor.execute("INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES ('Chino', 'Coniglio', 3, 1)")
mycursor.execute("INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES ('Orio', 'Orso', 300, 8)")


# Salvo le modifiche
mydb.commit()

print("5 animali inseriti con successo.")
