import translator as tr

t = tr.Translator()
check = True
t.loadDictionary("dictionary.txt")

while check:

    t.printMenu()
    txtIn = int(input("Che cosa desideri fare?: "))

    #Aggiungiamo parola
    if int(txtIn) == 1:
        parola = input("Perfavore aggiungi la parola nel formato:\n"
                       "Parola da tradurre [SPAZIO] traduzione: ")
        t.handleAdd(parola)
    #Cerchiamo una parola
    elif int(txtIn) == 2:
        parola = input("Scrivi la parola da cercare: ")
        t.handleTranslate(parola)
    #Cerchiamo con wildCard
    elif int(txtIn) == 3:
        parola = input("Scrivi la parola da cercare: ")
        t.handleWildCard(parola)
    elif int(txtIn) == 4:
        print("Grazie del tuo aiuto!")
        break
    else:
        print("Mi dispiace ma inserisci un numero da 1 a 4")

    #Chiedere se vuole continuare
    now = input("Desideri continuare?: ")
    if now == "no":
        print("Grazie del tuo aiuto!")
        check = False
