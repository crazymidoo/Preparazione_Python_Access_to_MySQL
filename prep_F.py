import mysql.connector

# Connessione al DB 'Animali'
mydb = mysql.connector.connect(
    host = "localhost",
    user = "pythonuser",
    password = "password123",
    database = "Animali"
)

mycursor = mydb.cursor()

# Chiedo all'utente quanti animali vuole inserire
# Utilizzo anche il Try Except per verificare che l'input sia corretto
try:
    n = int(input("Quanti animali vuoi inserire? "))
except ValueError:
    print("Devi inserire un numero intero valido. ")
    # Ho usato exit 1 per terminare il programma con un errore generico
    exit(1) # Usando break non funziona, ho scoperto che funziona solo se si è all'interno di un ciclo, non in questo caso

# Per il numero di volte che inserisce l'utente vai a fare... 
for i in range(n):
    print("Inserisci i dati del nuovo animale: ")
    nome = input("Nome_Proprio: ")
    razza = input("Razza: ")

    try:
        peso = int(input("Peso (kg): "))
        eta = int(input("Età (anni): "))
    except ValueError:
        print("Errore: Peso e Età devono essere numero interi. ")
        continue

    sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    val = (nome, razza, peso, eta)
    mycursor.execute(sql, val)

mydb.commit()

print(f"{n} animali inseriti con successo. ") # Quando avvio e metto valori non int in peso o età dopo il messaggio di errore ho il problema che appare pure questo dopo