class Adjacente:
    def __init__(self, cidade, distancia):
        self.cidade = cidade
        self.distancia = distancia
        self.distanciaEstrela = self.cidade.distanciaDesejada + self.distancia