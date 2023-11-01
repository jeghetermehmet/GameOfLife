from verden import Verden

def hovedprogram():
    rad = int(input("Skriv raden til rutenettet:"))
    kol = int(input("Skriv kolonnet til rutenettet:"))
    verden = Verden(rad, kol)
    verden.tegn()
    svar = 0
    while svar != "q":
        svar = input("Oppgi en tom linje for neste steg, eller q for å avslutte programmet: ")
        verden.oppdatering()
        verden.tegn()
    pass

# starte hovedprogrammet
hovedprogram()