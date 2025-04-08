from models.cardapio.itens import Itens

class Prato(Itens):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao
    
    def __str__(self):
        return self._nome