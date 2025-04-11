from models.cardapio.itens import Itens

class Bebida(Itens):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self.preco -= (self.preco * 0.05)