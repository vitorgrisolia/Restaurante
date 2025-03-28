# print('Python na Escola de Programação da Alura \n')
# nome = 'vitor'
# idade = 33
# print(f'Meu nome é {nome} e tenho idade {idade} anos \n')
# print('A \n')
# print('L \n')
# print('U \n')
# print('R \n')
# print('A \n')
# pi = 3.14159
# print('O valor arredondado de pi é:', round(pi, 2))


# def numero_impar_par():
#     print('Verificação do numero Impar ou Par \n')

# def logica_numero():
#     numero = int(input('Digite um número: \n'))
#     if numero % 2 == 0:
#         print(f'O numero que digitou {numero} é Par')
#     else:
#         print(f'O numero que digitou {numero} é Impar')

# def main():
#     numero_impar_par()
#     logica_numero()

# if __name__ == '__main__':
#     main()


# def categoria_usuario():
#     print('Categoria de Usuário por idade \n')

# def logica_usuario():
#     idade = int(input('Digite a sua idade para Classificar: \n'))

#     if idade <= 12:
#         print(f'Criança, idade digitada {idade}')
#     elif 13 <= idade <= 18:
#         print(f'Adolescente, idade digitada {idade}')
#     else:
#         print(f'Adulto, idade digitada {idade}')

# def main():
#     categoria_usuario()
#     logica_usuario()

# if __name__ == '__main__':
#     main()


# def verificar_login():
#     print('Verificador de Usuário e senha \n')

# usuario_correta = "admin"
# senha_correta = 123
# usuario = input('Digite o nome de Usuário: ')
# senha = int(input('Digite a senha de Usuário: '))

# def logica_verificacao():
#     if usuario == usuario_correta and senha == senha_correta:
#         print('Acesso Permitido')
#     else:
#         print('Usuário ou Senha INCORRETO, Acesso negado')


# def main():
#     verificar_login()
#     logica_verificacao()

# if __name__ == '__main__':
#     main()


def coordenadas_carteseano():
    print('Plano Carteseano')

def logica_carteseana():
    x = float(input("Digite a coordenada x: "))
    y = float(input("Digite a coordenada y: "))

    if x > 0 and y > 0:
        print("O ponto está no primeiro quadrante.")
    elif x < 0 and y > 0:
        print("O ponto está no segundo quadrante.")
    elif x < 0 and y < 0:
        print("O ponto está no terceiro quadrante.")
    elif x > 0 and y < 0:
        print("O ponto está no quarto quadrante.")
    else:
        print("O ponto está sobre um eixo ou na origem.")


def main():
    coordenadas_carteseano()
    logica_carteseana()

if __name__ == '__main__':
    main()