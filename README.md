# Trabalho CRUD - Victor Borges de Alencar

## Descrição do Projeto

Código em Python que permite gerenciar um banco de dados de jogadores de futebol. O código oferece funcionalidades completas de CRUD (Create, Read, Update, Delete), permitindo ao usuário adicionar, listar, atualizar e excluir jogadores, além de oferecer opções de filtragem para facilitar a busca por informações específicas por meio de uma CLI.

## Funcionalidades

O projeto oferece um menu interativo com as seguintes opções:

  * **Adicionar Jogador:** Permite registrar um novo jogador no banco de dados, solicitando informações como nome, idade, time, posição e nacionalidade.
  * **Listar Jogadores:** Exibe uma lista de todos os jogadores cadastrados no banco de dados.
  * **Listar Jogadores por Filtro:** Oferece um submenu para listar jogadores com base em critérios específicos:
      * Por time
      * Por posição
      * Por nacionalidade
      * Por nome
  * **Atualizar Jogador:** Permite modificar as informações de um jogador existente a partir do seu ID.
  * **Excluir Jogador:** Remove um jogador do banco de dados com base no seu ID.
  * **Sair:** Encerra a aplicação.

## Tecnologias Utilizadas

  * **Python:** Linguagem de programação principal do projeto.
  * **SQLite:** Sistema de gerenciamento de banco de dados utilizado para armazenar os dados dos jogadores.

## Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    ```
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd CRUD_Individual
    ```
3.  **Execute o arquivo principal:**
    ```bash
    python main.py
    ```

## Estrutura do Projeto

  * `main.py`: Contém a lógica da interface do usuário, como o menu principal e as funções que capturam a entrada do usuário.
  * `banco.py`: Responsável por toda a interação com o banco de dados SQLite, incluindo a criação da tabela e as operações de CRUD.
  * `banco.db`: Arquivo do banco de dados SQLite gerado na primeira execução do programa.
 
