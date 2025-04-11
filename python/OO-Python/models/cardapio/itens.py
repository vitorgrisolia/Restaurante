from abc import ABC, abstractmethod
from typing import List

class Itens:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"
    
    @abstractmethod
    def aplicar_desconto(self):
        pass