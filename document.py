blCrna = "CCAGCAATCGC"
blRjava = "GCCAGTGCCG"
blKoren = "TTAGCTATCGC"

ooKvadrat = "GCCACGG"
ooOkrogel = "ACCACAA"
ooOvalen = "AGGCCTCA"

boModra = "TTGTGGTGGC"
boZelena = "GGGAGGTGGC"
boRjava = "AAGTAGTGAC"

spM = "TGCAGGAACTTC"
spZ = "TGAAGGACCTTC"

rBel = "AAAACCTCA"
rCrn = "CGACTACAG"
rAzj = "CGCGGGCCG"


datoteka = open("tekst.txt", "r").read()

if datoteka.find(spM) and datoteka.find(rBel) and datoteka.find(blKoren)\
        and datoteka.find(boRjava) and datoteka.find(ooOkrogel) != -1:
    print("Sladoled je pojedel Ziga!")
elif datoteka.find(spM) and datoteka.find(rBel) and datoteka.find(blCrna)\
        and datoteka.find(boModra) and datoteka.find(ooOvalen) != -1:
    print("Sladoled je pojedel Matej!")
elif datoteka.find(spM) and datoteka.find(rBel) and datoteka.find(blRjava)\
        and datoteka.find(boZelena) and datoteka.find(ooKvadrat) != -1:
    print("Sladoled je pojedel Miha!")

print("Hitro v trgovino po novega!!!")
