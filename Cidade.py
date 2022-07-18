class Cidade:
    def __init__(self, nome, distanciaDesejada):
        self.nome = nome
        self.distanciaDesejada = distanciaDesejada
        self.visitado = False
        self.adjacentes = []
        
        
    def addCidadeAdjacente(self, cidade):
        self.adjacentes.append(cidade)
        
