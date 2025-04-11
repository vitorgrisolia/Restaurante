from models.avaliacao import Avaliacao
from models.cardapio.itens import Itens
from models.cardapio.sobremessa import Sobremessa

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        self._sobremessa = []
        self._sobremessa = Sobremessa
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'Restaurante: {self._nome} - Categoria: {self._categoria} - Ativo: {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print('Listando Restaurantes:')
        print('------------------------------------')
        print(f'{'Restaurante'.ljust(38)} | {'Categoria'.ljust(36)} | {'Status'.ljust(25)} | {'Avaliação'} \n')
        for restaurante in cls.restaurantes:
            print(f'Restaurante: {restaurante._nome.ljust(25)} - Categoria: {restaurante._categoria.ljust(25)} - Ativo: {restaurante.ativo.ljust(17)} | Avaliação: {restaurante.media_avaliacao} \n')
    
    @property
    def ativo(self):
        return '✅' if self._ativo else '❎'
    
    def ativar(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            raise ValueError('Nota deve ser entre 0 e 5')
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        quantidade_notas = len(self._avaliacao)
        soma_notes = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma_notes / quantidade_notas, 1)
        return media
    
    # def addicionar_bebida_cardapio(self, bebida):
    #     self._cardapio.appdend(bebida)
    
    # def addicionar_prato_cardapio(self, prato):
    #     self._cardapio.append(prato)

    def addiconar_cardapio(self, item):
        """Adiciona um item ao cardápio do restaurante."""
        if isinstance(item,Itens):
            self._cardapio.append(item)

    # @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome} - Categoria {self._categoria}:\n')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i} - {item.nome} - R$ {item.preco:.2f} - Descrição: {item.descricao}'
                print(mensagem_prato)
            elif hasattr(item, 'tamanho'):
                mensagem_bebida = f'{i} - {item.nome} - R$ {item.preco:.2f} - Tamanho: {item.tamanho}'
                print(mensagem_bebida)
            elif hasattr(item, 'tipo'):
                mensagem_sobremessa = f'{i} - {item.nome} - R$ {item.preco:.2f} - Tipo: {item.tamanho} - Tamanho: {item.tipo} - Descrição: {item.descricao}'
                print(mensagem_sobremessa)
            else:
                print(f'{i} - {item.nome} - R$ {item.preco:.2f}');