from models.restaurante import Restaurante

restaurante_praca = Restaurante('Praça do Sol', 'Comida Brasileira')
restaurante_mixcana = Restaurante('Mix Culinário', 'Comida Mexicana')
restaurante_japonesa = Restaurante('Sushi Brasil', 'Comida Japonesa')
restaurante_mixcana.ativar()

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()