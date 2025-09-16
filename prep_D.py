import mysql.connector

# Connessione al DB 'Animali'
mydb = mysql.connector.connect(
    host = "localhost",
    user = "pythonuser",
    password = "password123",
    database = "Animali"
)

mycursor = mydb.cursor()

for i in range(5):
    print("Inserisci un nuovo animale: ")

    nome = input("Nome_Proprio: ")
    razza = input("Razza: ")

    # PUNTO B OPZIONALE: Uso il Try Except per verificare Input
    try:
        peso = int(input("Peso (kg): "))
        eta = int(input("Età (anni): "))
    except ValueError:
        print("Errore: Peso e Età devono essere numeri interi. ")
        continue


    sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    val = (nome, razza, peso, eta)
    mycursor.execute(sql, val)

# Per salvare le modifiche utilizzo .commit()
mydb.commit()

print("5 animali inseriti con successo. ")