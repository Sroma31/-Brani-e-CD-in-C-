import brano 


class playlist:

    def __init__(self, nome):
        self.nome = nome
        self.brani = []

    
    def to_string(self):
        return f"Playlist: {self.nome}, Brani: {[brano.to_string() for brano in self.brani]} \n"

    def aggiungi_brano(self, brano):
        self.brani.append(brano)

    def rimuovi_brano(self, brano):
        if brano in self.brani:
            self.brani.remove(brano)
        else:
            print(f"Il brano '{brano.titolo}' non è presente nella playlist.")


    def durata_totale(self):
        # potrei scrivere
        # new duration=0
        # for brano in self.brani:
        #     duration+=brano.durata
        # return duration
        durata = sum(brano.durata for brano in self.brani)
        return durata



    def filtra_brani_per_autore(self, autore):
        newList=[]
        for brano in self.brani:
            if brano.autore == autore:
                newList.append(brano)
        return newList
        # oppure
        # return [brano for brano in self.brani if brano.autore == autore]
    



    def get_brani(self):
        return [str(brano) for brano in self.brani]



    

    