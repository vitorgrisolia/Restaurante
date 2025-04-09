from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça do Sol', 'Comida Brasileira')
restaurante_praca.ativar()
restaurante_praca.listar_restaurantes()
bebida_suco = Bebida('Suco de Laranja', 5.0, '300ml')
prato_bife = Prato('Bife Acebolado', 25.00, 'Bife com cebola e arroz')
restaurante_praca.addiconar_cardapio(bebida_suco)
restaurante_praca.addiconar_cardapio(prato_bife)


def main():
    restaurante_praca.exibir_cardapio()
    print('------------------------------------')

if __name__ == "__main__":
    main()