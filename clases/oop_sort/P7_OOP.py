class Caja:
    def __init__(self,peso_max):
        self.peso_max = peso_max
        self.muestras = []
    def agregar_muestra(self, muestra):
        if len(self.muestras) == 0 and muestra.peso <= self.peso_max:
            self.muestras.append(muestra)
            return True
        peso_total = 0
        for m in self.muestras:
            peso_total += m.peso
        peso_restante = self.peso_max - peso_total
        if muestra.peso <= peso_restante and muestra.riesgo() == self.muestras[0].riesgo():
            self.muestras.append(muestra)
            return True
        return False
    def contar_fragiles(self):
        cantidad = 0
        for m in self.muestras:
            if m.fragil:
                cantidad += 1
        return cantidad