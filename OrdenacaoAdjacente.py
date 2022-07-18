from Mapa import Mapa


class OrdenacaoAdjacente:
    def __init__(self, tamanho):
        self.numElementos = 0
        self.adjacentes = [None] * tamanho

    def inserir(self, adjacente):
        if self.numElementos == 0:
            self.adjacentes[0] = adjacente
            self.numElementos = 1
            return

        posicao = 0
        i = 0
        while i < self.numElementos:
            if (adjacente.distanciaEstrela > self.adjacentes[posicao].distanciaEstrela):
                posicao += 1
            i += 1

        for k in range(self.numElementos, posicao, -1):
            self.adjacentes[k] = self.adjacentes[k - 1]

        self.adjacentes[posicao] = adjacente
        self.numElementos += 1

    def getPrimeiro(self):
        return self.adjacentes[0].cidade

    def mostrar(self):
        for i in range(0, self.numElementos):
            print('{} - {}'.format(self.adjacentes[i].cidade.nome, self.adjacentes[i].distanciaEstrela))


