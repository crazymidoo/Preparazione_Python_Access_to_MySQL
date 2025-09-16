import mysql.connector

# Di nuovo connessione al DB 'Animali'
mydb = mysql.connector.connect(
    host="localhost",
    user="pythonuser",
    password="password123",
    database="Animali"
)

mycursor = mydb.cursor()

# A questo punto vado a creare il menù e uso un ciclo While
while True:
    print("----------  Menù:  ----------")
    print("1 - Inserisci un nuovo animale: ")
    print("2 - Visualizza tutti gli animali: ")
    print("3 - Elimina un animale: ")
    print("4 - Modifica un animale: ")

    # La scelta dell'utente è sicuramente un input
    scelta = input("Scegli un opzione: ")

    # Adesso l'utente avrà inserito un opzione, creiamo le condizioni per ogni scelta
    # Quindi usiamo l' IF
    if scelta == '1':
        nome = input("Nome_Proprio: ")
        razza = input("Razza: ")
        peso = input("Peso (kg): ")
        eta = input("Età (anni): ")

        #Try except in caso l'utente non inserisce un valore intero per il peso e per l'età
        try:
            peso = int(peso)
            eta = int(eta)
        except:
            print("Peso e Età devono essere n interi\n")
            continue  # Torna all'inizio del ciclo per riprovare perchè uso continue

        # Inserisco i dati nel database con query parametrizzata
        sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
        val = (nome, razza, peso, eta)
        mycursor.execute(sql, val)
        mydb.commit()  # Confermo la modifica nel database con il solito commit
        print("Animale inserito.\n")

    # Se invece l'utente sceglie 2??
    elif scelta == '2':
        # Per visualizzare tutti gli animali selezioniamo tutto con * dalla tabella Mammiferi
        mycursor.execute("SELECT * FROM Mammiferi")
        risultati = mycursor.fetchall() 
        # Ciclo for per stampare tutti i risultati
        for r in risultati:
            print(f"Id: {r[0]}, Nome: {r[1]}, Razza: {r[2]}, Peso: {r[3]}, Età: {r[4]}")
        print() # Questo l'ho messo per avere l'output più ordinato almeno stampa una riga vuota
    
    # E se sceglie 3?
    elif scelta == '3':
        id_da_eliminare = input("Inserisci l'id dell'animale da eliminare: ")
        try:
            id_da_eliminare = int(id_da_eliminare)
        except:
            print("Id deve essere un numero intero!\n")
            continue  # Torna all'inizio del ciclo per riprovare

        # Eseguo la query di cancellazione basandomi sull'id inserito dall'utente
        mycursor.execute("DELETE FROM Mammiferi WHERE Id = %s", (id_da_eliminare,))
        mydb.commit()  # Confermo la cancellazione sempre con il solito .commit()
        print("Animale eliminato.\n")

    # Infine se sceglie 4...
    elif scelta == '4':
        id_da_modificare = input("Inserisci l'id dell'animale da modificare: ")
        # Sempre il Try Except per gestire valori non validi che possono essere inseriti dall'utente
        try:
            id_da_modificare = int(id_da_modificare)
        except:
            print("Id deve essere un numero intero!\n")
            continue  # Torna all'inizio del ciclo per riprovare

        print("Inserisci i nuovi dati:")
        nome = input("Nome_Proprio: ")
        razza = input("Razza: ")
        peso = input("Peso (kg): ")
        eta = input("Età (anni): ")

        try:
            peso = int(peso)
            eta = int(eta)
        except:
            print("Peso e Età devono essere numeri interi!\n")
            continue  # Torna all'inizio del ciclo per riprovare

        # Eseguo l'update dei dati dell'animale con l'id specificato dall'utente
        sql = "UPDATE Mammiferi SET Nome_Proprio=%s, Razza=%s, Peso=%s, Eta=%s WHERE Id=%s"
        val = (nome, razza, peso, eta, id_da_modificare)
        mycursor.execute(sql, val)
        mydb.commit()  # Confermo la modifica ancora il .commit() di sempre
        print("Animale modificato (se esisteva).\n")

    else:
        print("Scelta non valida, riprova.\n")  # Gestione scelta non prevista

## Fine!
