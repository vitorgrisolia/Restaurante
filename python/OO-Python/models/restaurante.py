class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'Restaurante: {self._nome} - Categoria: {self._categoria} - Ativo: {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print('Listando Restaurantes:')
        print('------------------------------------')
        print(f'{'Restaurante'.ljust(38)} | {'Categoria'.ljust(36)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'Restaurante: {restaurante._nome.ljust(25)} - Categoria: {restaurante._categoria.ljust(25)} - Ativo: {restaurante.ativo}')
    
    @property
    def ativo(self):
        return '✅' if self._ativo else '❎'
    
    def ativar(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça do Sol', 'Comida Brasileira')
restaurante_praca.ativar()
restaurante_pizza = Restaurante('Pizza Hut', 'Comida Italiana')