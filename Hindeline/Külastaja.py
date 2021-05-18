from Hindeline.Raamat import Raamat

class Külastaja:
    def __init__(self,eesNimi, perekonnaNimi):
    #Kodutöö omadused:
        self.eesnimi = eesNimi
        self.perekonnanimi = perekonnaNimi
        self.laenutatudRaamatud = []

    def laenutaRaamat (self, Lugemine):
        self.laenutatudRaamatud.append(Lugemine)


Külastaja1 = Külastaja("Joosep", "Joosepson")

Raamat1 = Raamat("Atlas", "Wusser", 305)
Raamat2 = Raamat("Romaan", "Susser", 400)


Külastaja1.laenutaRaamat(Raamat1)
Külastaja1.laenutaRaamat(Raamat2)





