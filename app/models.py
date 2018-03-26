class Categ:#Categoria
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class Prod: #Produto
    def __init__(self, id, nome, qtde, preco, data, id_categ):
        self.id = id
        self.nome = nome
        self.qtde = qtde
        self.preco = preco
        self.data = data
        self.id_categ = id_categ

