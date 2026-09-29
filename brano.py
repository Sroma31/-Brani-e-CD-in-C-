class brano:
    #init è il costruttore della classe brano, che viene chiamato quando si crea un nuovo oggetto di tipo brano.
    def __init__(self, titolo, autore, durata):
        self.titolo = titolo
        self.autore = autore
        self.durata = durata


    #getter e setter.
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
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Durata: {self.durata}"   

    def shortSong(self):
        return f"{self.titolo} - {self.autore}"


    