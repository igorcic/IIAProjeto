from OrdenacaoVector import OrdenacaoVector
from Mapa import Mapa


class BuscaGulosa:
    def __init__(self, chegada):
        self.chegada = chegada
        self.achou = False

    def buscar(self, atual):
        print('\nAtual: {}'.format(atual.nome))

        if atual == self.chegada:
            self.achou = True
        else:
            self.fronteira = OrdenacaoVector(len(atual.adjacentes))
            for a in atual.adjacentes:
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.inserir(a.cidade)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                BuscaGulosa.buscar(self, self.fronteira.getPrimeiro())


mapa = Mapa()
mapa_chegada = BuscaGulosa(mapa.bucharest)
mapa_chegada.buscar(mapa.arad)
