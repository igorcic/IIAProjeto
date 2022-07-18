from Mapa import Mapa


class OrdenacaoVector:
    def __init__(self, tamanho):
        self.numElementos = 0
        self.cidades = [None] * tamanho

    def inserir(self, cidade):
        if self.numElementos == 0:
            self.cidades[0] = cidade
            self.numElementos = 1
            return

        posicao = 0
        i = 0
        while i < self.numElementos:
            if (cidade.distanciaDesejada > self.cidades[posicao].distanciaDesejada):
                posicao += 1
            i += 1

        for k in range(self.numElementos, posicao, -1):
            self.cidades[k] = self.cidades[k - 1]

        self.cidades[posicao] = cidade
        self.numElementos += 1

    def getPrimeiro(self):
        return self.cidades[0]

    def mostrar(self):
        for i in range(0, self.numElementos):
            print('{} - {}'.format(self.cidades[i].nome, self.cidades[i].distanciaDesejada))


