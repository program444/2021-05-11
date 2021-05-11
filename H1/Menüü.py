from H1.Toit import Toit

#alamklass Menüü:
class Menüü:
    def __init__(self, pealkirjaNimetus):
        self.Pealkiri = pealkirjaNimetus
        self.toidud = []

    def lisaToit(self, Road):
        self.toidud.append(Road)

   #     return (lisaToit)

#    def tagastaToidud(self):
 #       for toit in self.toidud:
  #          print(toit.nimetus, "hind:", toit.hind, "päevaEri:", toit.eripakkumine)

    def kuvaToidudJaHinnad(self):
        for toit in self.toidud:
            print(toit.nimetus, "hind:", toit.hind, "päevaEri:", toit.eripakkumine)

    def kuvaPäevaEri(self):
        for toit in self.toidud:
            if toit.eripakkumine:
                print("Päeva Üllatus on:",toit.nimetus, "hind:", toit.hind, "päevaEri:", toit.eripakkumine)

    def leiaKallimToit(self):
        maximumHind = 0
        for toit in self.toidud:
            if toit.hind >= maximumHind:
                kalleimToit = toit
                maximumHind = toit.hind

        print(" kõige kallim toit on:", kalleimToit.nimetus, kalleimToit.hind)



päevaMenüü = Menüü("Ala carte menüü")

print(päevaMenüü.Pealkiri)

magustoiduMenüü = Menüü("Magustoidu menüü")

uusToit = Toit("redis",2, False)

päevaLemmik = Toit ("kapsas",1, False)

päevaÜllatus = Toit ("hapukapsasupp", 5, True)



päevaMenüü.lisaToit(uusToit)
päevaMenüü.lisaToit(päevaLemmik)
päevaMenüü.lisaToit(päevaÜllatus)
print(päevaMenüü.toidud)

print(magustoiduMenüü.Pealkiri)

#päevaMenüü.tagastaToidud()
#päevaMenüü.tagastaToidud()
päevaMenüü.kuvaToidudJaHinnad()
päevaMenüü.kuvaPäevaEri()
päevaMenüü.leiaKallimToit()








