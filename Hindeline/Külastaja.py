from Hindeline.Raamat import Raamat

class Külastaja:
    def __init__(self,eesNimi, perekonnaNimi):
    #Kodutöö omadused:
        self.eesnimi = eesNimi
        self.perekonnanimi = perekonnaNimi
        self.laenutatudRaamatud = []
        self.tagastatudRaamatud = []

    def laenutaRaamat (self, uusLugemine):
        self.laenutatudRaamatud.append(uusLugemine)



    def tagastaRaamat (self,laenutatudRaamatud):
        for tagastatudRaamat in self.laenutatudRaamatud:
            laenutatudRaamatud.laenutatud = True
            self.tagastaRaamat.append(laenutatudRaamatud)

    def tagastaRaamat (self,tagastusRaamat):
        self.laenutatudRaamatud.remove(tagastusRaamat)
        print(Külastaja1.eesnimi, Külastaja1.perekonnanimi, "tagastas raamatu:", tagastusRaamat.nimetus)

    def kuvaLaenutatudRaamatud(self):
        for laenusRaamat in self.laenutatudRaamatud:
            print("Laenus on raamat: pealkiri:", laenusRaamat.nimetus, "autor:",laenusRaamat.nimi,"lehekülgi:",laenusRaamat.leheküljed)





Külastaja1 = Külastaja("Joosep", "Joosepson")

laenatudRaamat1 = Raamat("Atlas", "Wusser", 305)
laenatudRaamat2 = Raamat("Romaan", "Susser", 400)


print(Külastaja1.eesnimi, Külastaja1.perekonnanimi, "laenutas raamatu:", laenatudRaamat1.nimetus, "mille autor on:",laenatudRaamat1.nimi)
print(Külastaja1.eesnimi, Külastaja1.perekonnanimi, "laenutas raamatu:",laenatudRaamat2.nimetus,"mille autor on:",laenatudRaamat2.nimi)
print(Külastaja1.eesnimi, Külastaja1.perekonnanimi, "tagastas raamatu:", laenatudRaamat2.nimetus)


Külastaja1.laenutaRaamat(laenatudRaamat1)
Külastaja1.laenutaRaamat(laenatudRaamat2)
#print(Külastaja1.laenutatudRaamatud)
Külastaja1.tagastaRaamat(laenatudRaamat1)
#print(Külastaja1.laenutatudRaamatud)
Külastaja1.kuvaLaenutatudRaamatud()
Külastaja1.laenutaRaamat(laenatudRaamat1)
Külastaja1.kuvaLaenutatudRaamatud()















