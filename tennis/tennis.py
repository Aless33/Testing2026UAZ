class TenisScore:
    def __init__(self):
        self.puntos = [0, 0]
        self.marcador = ['0', '15', '30', '40', 'Adv', 'Win', 'Deuce']

    def anotar(self, jugador):
        if jugador == 1:
            if self.puntos[0] == 3 and self.puntos[1] == 4:
                self.puntos[0] = 6
                self.puntos[1] = 6
            elif self.puntos[0] == 6 and self.puntos[1] == 6:
                self.puntos[0] = 4
                self.puntos[1] = 3
            else:
                self.puntos[0] += 1
        elif jugador == 2:
            if self.puntos[1] == 3 and self.puntos[0] == 4:
                self.puntos[1] = 6
                self.puntos[0] = 6
            elif self.puntos[1] == 6 and self.puntos[0] == 6:
                self.puntos[1] = 4
                self.puntos[0] = 3
            else:
                self.puntos[1] += 1

    def score(self):
        j1 = self.marcador[self.puntos[0]]
        j2 = self.marcador[self.puntos[1]]
        return f'{j1} - {j2}'