from OrdenacaoAdjacente import OrdenacaoAdjacente
from Mapa import Mapa


class BuscaAEstrela:
    def __init__(self, chegada):
        self.chegada = chegada
        self.achou = False

    def buscar(self, atual):
        print('\nAtual: {}'.format(atual.nome))
        atual.visitado = True

        if atual == self.chegada:
            self.achou = True
        else:
            self.fronteira = OrdenacaoAdjacente(len(atual.adjacentes))
            for a in atual.adjacentes:
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.inserir(a)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                 BuscaAEstrela.buscar(self, self.fronteira.getPrimeiro())


mapa = Mapa()
mapa_chegada = BuscaAEstrela(mapa.bucharest)
mapa_chegada.buscar(mapa.arad)