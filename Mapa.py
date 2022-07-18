from Cidade import Cidade
from Adjacente import Adjacente


class Mapa:
    arad = Cidade("Arad", 366)
    zerind = Cidade("Zerind", 374)
    timisoara = Cidade("Timisoara", 329)
    oradea = Cidade("Oradea", 380)
    lugoj = Cidade("Lugoj", 244)
    sibiu = Cidade("Sibiu", 253)
    meharia = Cidade("Mehadia", 241)
    dobreta = Cidade("Dobreta", 242)
    craviova = Cidade("Craviova", 160)
    rimnicu = Cidade("Rimnicu Vilcea", 193)
    pitesti = Cidade("Pitesti", 98)
    fagaras = Cidade("Fagaras", 178)
    giurgiu = Cidade("Giurgiu", 77)
    bucharest = Cidade("Bucharest", 0)
    urziceni = Cidade("Urziceni", 80)
    eforie = Cidade("Eforie", 161)
    hirsova = Cidade("Hirsova", 151)
    vaslui = Cidade("Vaslui", 199)
    iasi = Cidade("Iasi", 226)
    neamt = Cidade("Neamt", 234)

    arad.addCidadeAdjacente(Adjacente(zerind, 75))
    arad.addCidadeAdjacente(Adjacente(sibiu, 140))
    arad.addCidadeAdjacente(Adjacente(timisoara, 118))

    zerind.addCidadeAdjacente(Adjacente(oradea, 71))
    zerind.addCidadeAdjacente(Adjacente(arad, 75))

    timisoara.addCidadeAdjacente(Adjacente(lugoj, 111))
    timisoara.addCidadeAdjacente(Adjacente(arad, 118))

    sibiu.addCidadeAdjacente(Adjacente(fagaras, 99))
    sibiu.addCidadeAdjacente(Adjacente(rimnicu, 80))
    sibiu.addCidadeAdjacente(Adjacente(oradea, 151))
    sibiu.addCidadeAdjacente(Adjacente(arad, 140))

    oradea.addCidadeAdjacente(Adjacente(sibiu, 151))
    oradea.addCidadeAdjacente(Adjacente(zerind, 71))

    lugoj.addCidadeAdjacente(Adjacente(meharia, 70))
    lugoj.addCidadeAdjacente(Adjacente(timisoara, 111))

    fagaras.addCidadeAdjacente(Adjacente(bucharest, 211))
    fagaras.addCidadeAdjacente(Adjacente(sibiu, 99))

    rimnicu.addCidadeAdjacente(Adjacente(pitesti, 97))
    rimnicu.addCidadeAdjacente(Adjacente(sibiu, 80))

    meharia.addCidadeAdjacente(Adjacente(dobreta, 75))
    meharia.addCidadeAdjacente(Adjacente(lugoj, 70))

    dobreta.addCidadeAdjacente(Adjacente(craviova, 120))
    dobreta.addCidadeAdjacente(Adjacente(meharia, 75))

    craviova.addCidadeAdjacente(Adjacente(pitesti, 138))
    craviova.addCidadeAdjacente(Adjacente(rimnicu, 146))
    craviova.addCidadeAdjacente(Adjacente(dobreta, 120))

    pitesti.addCidadeAdjacente(Adjacente(bucharest, 101))
    pitesti.addCidadeAdjacente(Adjacente(craviova, 138))
    pitesti.addCidadeAdjacente(Adjacente(rimnicu, 97))

    bucharest.addCidadeAdjacente(Adjacente(urziceni, 85))
    bucharest.addCidadeAdjacente(Adjacente(pitesti, 101))
    bucharest.addCidadeAdjacente(Adjacente(fagaras, 211))
    bucharest.addCidadeAdjacente(Adjacente(giurgiu, 90))

    giurgiu.addCidadeAdjacente(Adjacente(bucharest, 90))

    urziceni.addCidadeAdjacente(Adjacente(vaslui, 142))
    urziceni.addCidadeAdjacente(Adjacente(hirsova, 98))
    urziceni.addCidadeAdjacente(Adjacente(bucharest, 85))

    hirsova.addCidadeAdjacente(Adjacente(eforie, 86))
    hirsova.addCidadeAdjacente(Adjacente(urziceni, 98))

    eforie.addCidadeAdjacente(Adjacente(hirsova, 86))

    vaslui.addCidadeAdjacente(Adjacente(urziceni, 142))
    vaslui.addCidadeAdjacente(Adjacente(iasi, 92))

    iasi.addCidadeAdjacente(Adjacente(neamt, 87))
    iasi.addCidadeAdjacente(Adjacente(vaslui, 92))

    neamt.addCidadeAdjacente(Adjacente(iasi, 87))


mapa = Mapa()
print(mapa.arad.nome)
print(mapa.arad.visitado)
for i in range(len(mapa.arad.adjacentes)):
    print(mapa.arad.adjacentes[i].cidade.nome)
