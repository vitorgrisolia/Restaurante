from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
from models.cardapio.sobremessa import Sobremessa

restaurante_praca = Restaurante('Praça do Sol', 'Comida Brasileira')
restaurante_praca.listar_restaurantes()
bebida_suco = Bebida('Suco de Laranja', 5.0, '300ml')
bebida_suco.aplicar_desconto()
prato_bife = Prato('Bife Acebolado', 25.00, 'Bife com cebola e arroz')
prato_bife.aplicar_desconto()
sobremessa = Sobremessa('Pudim', 10.00, 'Pedaço', 'DOce', 'torta de Banana com chocolate')
sobremessa.aplicar_desconto()
restaurante_praca.addiconar_cardapio(bebida_suco)
restaurante_praca.addiconar_cardapio(sobremessa)
restaurante_praca.addiconar_cardapio(prato_bife)


def main():
    restaurante_praca.exibir_cardapio()
    print('------------------------------------')

if __name__ == "__main__":
    main()