class Celle:
    # Konstruktør
    def __init__(self):
        self._status = "doed"
        self._naboer = []
        self._ant_levende_naboer = 0
    
    def sett_doed(self):
        self._status = "doed"

    def sett_levende(self):
        self._status = "levende"

    def er_levende(self):
        return self._status == "levende"

    def hent_status_tegn(self):
        if self.er_levende():
            return "O"
        return "."

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)

    def tell_levende_naboer(self):
        for nabo in self._naboer:
            if nabo is not None and nabo.er_levende():
                self._ant_levende_naboer += 1
        return self._ant_levende_naboer
    
    def oppdater_status(self):
        levende_naboer = self.tell_levende_naboer()
        if self.er_levende():
            if levende_naboer < 2 or levende_naboer > 3:
                self.sett_doed()
        else:
            if levende_naboer == 3:
                self.sett_levende()

