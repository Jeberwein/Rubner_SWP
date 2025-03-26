class Bucher:
    def __init__(self, titel, author, price):
        self.titel = titel
        self.author = author
        self.price = price


class Library:
    bucher = []

    @staticmethod
    def hinzu(buch):
        if isinstance(buch, Bucher):
            Library.bucher.append(buch)
            print(f"Buch '{buch.titel}' hinzugefügt")
        else:
            print("Das übergebene Objekt ist kein Buch!")

    @staticmethod
    def aendern(price, name):
        for buch in Library.bucher:
            if buch.titel == name:
                buch.price = price
                print(f"Preis von '{name}' geändert auf {price}")
                return
        print(f"Buch mit dem Titel '{name}' nicht gefunden")

    @staticmethod
    def delete(name):
        for buch in Library.bucher:
            if buch.titel == name:
                Library.bucher.remove(buch)
                print(f"Buch '{name}' erfolgreich gelöscht")
                return
        print(f"Buch mit dem Titel '{name}' nicht gefunden")

    @staticmethod
    def alle():
        if not Library.bucher:
            print("Es gibt keine Bücher in der Bibliothek.")
        else:
            print(f"Anzahl der Bücher: {len(Library.bucher)}")
            for buch in Library.bucher:
                print(f"Titel: {buch.titel}, Autor: {buch.author}, Preis: {buch.price}")


# Bücher erstellen
buch1 = Bucher("Buch A", "Autor A", 20)
buch2 = Bucher("Buch B", "Autor B", 30)

# Bücher hinzufügen
Library.hinzu(buch1)
Library.hinzu(buch2)

# Alle Bücher anzeigen
Library.alle()

# Preis eines Buches ändern
Library.aendern(25, "Buch A")

# Ein Buch löschen
Library.delete("Buch A")

# Aktuelle Bücher anzeigen
Library.alle()
