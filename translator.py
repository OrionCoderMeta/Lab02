
class Translator:

    def __init__(self):
        self.diz = {}

    def printMenu(self):
        print(f"1. Aggiungi nuova parola \n2. Cerca una parola \n3. Cerca con wildcard \n4. Exit")

    def loadDictionary(self, dict):
        with open(dict) as file:
            for line in file:
                line = line.strip().split(" ")
                if line[0] not in self.diz:
                    self.diz[line[0]] = [line[1]]
                else:
                    self.diz[line[0]].append(line[1])

    def handleAdd(self, entry):
        entry = entry.strip()
        entry = entry.split(" ")
        if entry[0] not in self.diz:
            self.diz[entry[0]] = [entry[1]]
            with open("dictionary.txt", "a") as file:
                file.write(f"{entry[0]} {entry[1]} \n")
            print("Grazie per la nuova parola!")
        elif entry[0] in self.diz and entry[1] not in self.diz[entry[0]]:
            self.diz[entry[0]].append(entry[1])
            with open("dictionary.txt", "a") as file:
                file.write(f"{entry[0]} {entry[1]} \n")
            print(f"Grazie per la nuova traduzione di {entry[0]} !")
        else:
            print("Grazie ma la tua traduzione già esiste nel sistema!")

    def handleTranslate(self, query):
        if query in self.diz:
            r = ""
            for el in self.diz[query]:
                r += (el + " ")
            print(f"Ecco la/le traduzioni: {r}")
        else:
            print("Mi dispiace ma la parola non ha traduzione :(")

    def handleWildCard(self, query):
        parola = query.replace("?", "")  # Rimuove il punto interrogativo
        traduzioni = []

        for word in self.diz:
            if parola in word:
                traduzioni.append(f"{word} : {', '.join(self.diz[word])}")

        if traduzioni:
            print(f"Le traduzioni per la parola '{query}' sono:\n" + "\n".join(traduzioni))
        else:
            print(f"Nessuna traduzione trovata per '{query}'")
