from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()
        
    def _lag_tomt_rutenett(self):
        ytre_liste = []
        i = 0
        while i < self._ant_rader:
            ytre_liste.append(self._lag_tom_rad())
            i += 1
        return ytre_liste

    def _lag_tom_rad(self):
        enkelliste = []
        i = 0
        while i < self._ant_kolonner:
            enkelliste.append(None)
            i += 1
        return enkelliste
    
    def fyll_med_tilfeldige_celler(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self.lag_celle(rad, kol)

    def lag_celle(self, rad, kol):
        celle = Celle()
        tilfeldigtall = randint(0, 2)
        if tilfeldigtall == 0:
            celle.sett_levende()
        self._rutenett[rad][kol] = celle

    def hent_celle(self, rad, kol):
        if (0 <= rad and rad < self._ant_rader) and (0 <= kol and kol < self._ant_kolonner):
            return self._rutenett[rad][kol]
        return None

    def tegn_rutenett(self):
        # Tøm terminalvinduet
        print("\n" * 10)
        for rader in range(self._ant_rader):
            for kolonner in range(self._ant_kolonner):
                celle = self.hent_celle(rader, kolonner)
                print(celle.hent_status_tegn(), end="")
            print()  # Legg til linjeskift etter hver rad

    def _sett_naboer(self, rad, kol):
        celle = self.hent_celle(rad, kol)  # Hent cellen på angitt rad og kolonne

        for r in range(rad - 1, rad + 2):
            for k in range(kol - 1, kol + 2):
                nabo = self.hent_celle(r, k)
                if nabo is not None and (r, k) != (rad, kol):
                    celle.legg_til_nabo(nabo)

    def koble_celler(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self._sett_naboer(rad, kol)

    def hent_alle_celler(self):
        alle_celler = []
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                celle = self.hent_celle(rad, kol)
                alle_celler.append(celle)
        return alle_celler


    def antall_levende(self):
        teller = 0
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                celle = self.hent_celle(rad, kol)
                if celle.er_levende():
                    teller += 1
        return teller
    
