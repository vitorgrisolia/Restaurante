# Sistema de Gerenciamento de Restaurantes

Bem-vindo ao **Sistema de Gerenciamento de Restaurantes**, um aplicativo simples em Python para cadastrar, listar e gerenciar o estado (ativo/desativado) de restaurantes. Este programa foi desenvolvido com uma interface de linha de comando (CLI) e é ideal para iniciantes que desejam aprender conceitos básicos de programação, como manipulação de listas, funções e controle de fluxo.

## Funcionalidades

O sistema oferece as seguintes opções:

*   **Cadastrar Restaurante**: Permite adicionar um novo restaurante à lista, informando seu nome e categoria.
*   **Listar Restaurantes**: Exibe uma tabela com os restaurantes cadastrados, incluindo nome, categoria e status (ativado/desativado).
*   **Alterar Estado do Restaurante**: Permite ativar ou desativar um restaurante existente com base no nome fornecido.
*   **Sair**: Encerra a execução do programa.

## Pré-requisitos

Para executar o programa, você precisa ter:

*   Python 3.x instalado em seu sistema.
*   Um terminal ou ambiente de desenvolvimento (como VS Code, PyCharm ou IDLE).
*   Nenhuma biblioteca externa é necessária, pois o código utiliza apenas o módulo `os` padrão para limpar a tela.

## Como Executar

1.  Clone ou copie o código para um arquivo com extensão `.py` (exemplo: `restaurantes.py`).
2.  Abra o terminal na pasta onde o arquivo está salvo.
3.  Execute o programa com o comando:
    ```bash
    python restaurantes.py
    ```
    ou
    ```bash
    python3 restaurantes.py
    ```
    (depende da configuração do seu sistema).
4.  O programa exibirá um banner e um menu com as opções disponíveis. Digite o número correspondente à ação desejada e siga as instruções na tela.

## Estrutura do Código

### Variáveis Globais

*   `restaurantes`: Uma lista de dicionários que armazena os dados dos restaurantes. Cada restaurante (dicionário) possui as chaves:
    *   `nome`: Nome do restaurante (`string`).
    *   `categoria`: Categoria do restaurante (`string`).
    *   `ativo`: Estado do restaurante (`boolean`: `True` para ativado, `False` para desativado).

### Funções Principais

*   `exibir_nome_do_programa()`: Mostra um banner ASCII com o nome do programa.
*   `exibir_opcoes()`: Exibe o menu com as opções disponíveis.
*   `cadastrar_novo_restaurante()`: Solicita o nome e a categoria do restaurante e o adiciona à lista `restaurantes`.
*   `listar_restaurantes()`: Mostra todos os restaurantes cadastrados em formato de tabela.
*   `alterar_estado_restaurante()`: Altera o estado (`ativo`/`desativo`) de um restaurante com base no nome fornecido pelo usuário.
*   `escolher_opcao()`: Gerencia a interação do usuário com o menu e chama as funções correspondentes à opção escolhida.
*   `main()`: Função principal que inicializa o programa chamando `exibir_nome_do_programa()` e `exibir_opcoes()`.

### Funções Auxiliares

*   `exibir_subtitulo(texto)`: Exibe um subtítulo formatado com linhas de asteriscos.
*   `voltar_ao_menu_principal()`: Pausa a execução e aguarda o usuário pressionar Enter para retornar ao menu principal.
*   `opcao_invalida()`: Exibe mensagem de erro para opções inválidas no menu principal.
*   `opcao_invalida_numero()`: Exibe mensagem de erro para entradas não numéricas quando um número é esperado.
*   `finalizar_app()`: Encerra o programa exibindo uma mensagem de finalização.

## Exemplo de Uso

Ao executar o programa, você verá algo assim:

```text
# ░██████╗░█████╗░██████╗░░█████╗░██████╗░
# ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
# ╚█████╗░███████║██████╦╝██║░░██║██████╔╝
# ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
# ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║░

1. Cadastrar restaurante
2. Listar restaurantes
3. Alterar Estado do restaurante
4. Sair

Escolha uma opção:

## Limitações
Persistência: O programa não persiste os dados. Os restaurantes cadastrados são armazenados apenas na memória durante a execução e são perdidos ao fechar o programa.

Validação: Não há validação avançada para entradas (como nomes duplicados, categorias padronizadas ou tratamento de campos vazios).

Portabilidade da Limpeza de Tela: Funciona melhor em sistemas Windows devido ao comando os.system('cls'). Em sistemas Unix/Linux (como macOS ou distribuições Linux), o ideal é substituir por os.system('clear') para limpar o terminal corretamente.

## Possíveis Melhorias
Adicionar persistência de dados salvando/carregando a lista de restaurantes em um arquivo (ex.: JSON, CSV ou um banco de dados simples como SQLite).

### Implementar validação de entradas para evitar erros (ex: não permitir nomes duplicados, garantir que a categoria não esteja vazia).

### Adicionar opções para editar informações de um restaurante existente ou excluir um restaurante.

### Melhorar a interface do usuário, talvez utilizando uma biblioteca como rich para uma CLI mais elaborada, ou criar uma versão gráfica com Tkinter ou PyQt.

### Refatorar o código para usar Programação Orientada a Objetos (OOP), criando uma classe Restaurante.

## Contribuições
Sinta-se à vontade para sugerir melhorias, reportar bugs ou enviar pull requests! Este é um projeto simples e aberto para aprendizado e colaboração.

## Licença
Este projeto é de uso livre para fins educacionais e de aprendizado. Não possui uma licença formal definida (pode-se considerar como domínio público ou adicionar uma licença como MIT se desejar formalizar).