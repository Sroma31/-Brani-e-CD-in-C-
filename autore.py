class autore:

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def set_nome(self, nome):
        self.nome = nome

    def set_cognome(self, cognome):
        self.cognome = cognome

    def to_string(self):
        return f"Nome: {self.nome}, Cognome: {self.cognome}"