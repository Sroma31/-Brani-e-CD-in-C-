import autore 

class brano:

    def __init__(self, titolo, autore, durata):
        self.titolo = titolo
        self.autore = autore
        self.durata = durata

    def get_titolo(self):
        return self.titolo

    def get_autore(self):
        return self.autore

    def get_durata(self):
        return self.durata

    def set_titolo(self, titolo):
        self.titolo = titolo

    def set_autore(self, autore):
        self.autore = autore

    def set_durata(self, durata):
        self.durata = durata

    def to_string(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore.get_nome()} {self.autore.get_cognome()}, Durata: {self.durata} minuti"