import sqlite3
import sys
import banco as db
import os


def menu(): 
    print("--- Menu de Opções ---\n")
    print("1. Adicionar Jogador")
    print("2. Listar Jogadores")
    print("3. Listar Jogadores por Filtro")
    print("4. Atualizar Jogador")
    print("5. Excluir Jogador")
    print("6. Sair")

def inserir_jogador():
    os.system('cls')
    print("Digite 'cancelar' ou '0' para voltar ao menu principal") 
    nome = input("\nQual o nome do jogador?\n").strip()
    if nome.lower() == "cancelar" or nome == '0': #volta ao menu principal
        return
    while(True): #testa se digitou numero
        try:
            idade = int(input(f"\nQual a idade do {nome}?\n")) #converte string para int
            if idade == 0:
                return
            break #sai do loop
        except ValueError:
            os.system('cls')
            print("Digite um valor numérico inteiro ou 0 para voltar ao menu principal.\n")
    time = input(f"\nQual o time atual do {nome}?\n").strip()
    if time.lower() == "cancelar" or time == '0': #volta ao menu principal
        return
    posicao = input(f"\nQual posição o {nome} joga? Escreva em até 3 letras (CAM, CDM, ST, LW, RW, etc)\n").strip()
    if posicao.lower() == "cancelar" or posicao == '0': #volta ao menu principal
        return
    nacionalidade = input(f"\nQual a nacionalidade do {nome}? \n").strip()
    if nacionalidade.lower() == "cancelar" or nacionalidade == '0': #volta ao menu principal
        return
    db.inserir_jogador(nome, idade, time, posicao, nacionalidade) #insere dados com o banco.py

###
def listar_jogador():
    if db.verificar_banco_vazio(): #se o banco estiver vazio
        print("\nNenhum jogador cadastrado no banco. Pressione Enter para retornar ao menu.\n")
        input()
        return
    db.listar_jogador()

def menu_listar():
    print("--- Menu de Listas ---\n")
    print("1. Por id")
    print("2. Por nome")
    print("3. Por time")
    print("4. Por posição")
    print("5. Por nacionalidade")
    print("6. Voltar")

def listar_jogador_filtro():
    if db.verificar_banco_vazio(): #se o banco estiver vazio
        print("\nNenhum jogador cadastrado no banco. Pressione Enter para retornar ao menu.\n")
        input()
        return
    
    while(True): #mantem o menu de listar ativo
        os.system('cls')
        menu_listar()
        opcao = input("\nComo deseja listar os jogadores?\n")
        match opcao:
            case "1":
                listar_jogador_id()
            case "2":
                listar_jogador_nome()
            case "3":
                listar_jogador_time()
            case "4":
                listar_jogador_posicao()
            case "5":
                listar_jogador_nacionalidade()
            case "6":
                return #finaliza a funcao atual e volta para a main(nesse caso, o listar_jogador_filtro --> esta no primeiro menu)
            case _: #caso nao escolha um numero do menu
                os.system('cls')
                print("\nOpção Inválida. Por favor, selecione uma das opções exibidas.")

def listar_jogador_id():
    db.listar_jogador_id()

def listar_jogador_nome():
    db.listar_jogador_nome()

def listar_jogador_time():
    db.listar_jogador_time()

def listar_jogador_posicao():
    db.listar_jogador_posicao()

def listar_jogador_nacionalidade():
    db.listar_jogador_nacionalidade()

###
def atualizar_jogador():
    if db.verificar_banco_vazio(): #se o banco estiver vazio
        print("\nNenhum jogador cadastrado no banco. Pressione Enter para retornar ao menu.\n")
        input()
        return
    
    db.listar_jogador() #mostra a lista de jogadores
    print("\nDigite 'cancelar' ou '0' para voltar ao menu principal")
    while(True): #testa se digitou numero
        try:
            id = int(input("\nQual o ID do jogador que deseja atualizar?\n")) #converte string para int
            if id == 0: #int nao precisa de aspas
                return
            break #sai do loop
        except ValueError:
            os.system('cls')
            print("Digite um valor numérico inteiro ou 0 para voltar ao menu principal.\n")
    
    if not db.verificar_jogador(id): #se o jogador nao existir
        print(f"\nJogador com ID {id} não encontrado. Pressione Enter para retornar ao menu.\n")
        input() #pausa a tela
        return

    new_nome = input("\nQual o novo nome do jogador?\n").strip()
    if new_nome.lower() == "cancelar" or new_nome == '0': #volta ao menu principal
        return
    while(True): #testa se digitou numero
        try:
            new_idade = int(input(f"\nQual a nova idade do {new_nome}?\n")) #converte string para int
            if new_idade == 0: #int nao precisa de aspas
                return
            break #sai do loop
        except ValueError:
            os.system('cls')
            print("Digite um valor numérico inteiro ou 0 para voltar ao menu principal.\n")

    new_time = input(f"\nQual o novo time atual do {new_nome}?\n").strip()
    if new_time.lower() == "cancelar" or new_time == '0': #volta ao menu principal
        return
    
    new_posicao = input(f"\nQual a nova posição que o {new_nome} joga? Escreva em até 3 letras (CAM, CDM, ST, LW, RW, etc)\n").strip()
    if new_posicao.lower() == "cancelar" or new_posicao == '0': #volta ao menu principal
        return
    
    new_nacionalidade = input(f"\nQual a nova nacionalidade do {new_nome}? \n").strip()
    if new_nacionalidade.lower() == "cancelar" or new_nacionalidade == '0': #volta ao menu principal
        return
    
    db.atualizar_jogador(id, new_nome, new_idade, new_time, new_posicao, new_nacionalidade)
    db.listar_jogador() #mostra a lista atualizada

    print("\nJogador atualizado com sucesso!\nPressione Enter para retornar ao menu.\n")
    input() #pausa a tela

def excluir_jogador():
    if db.verificar_banco_vazio(): #se o banco estiver vazio
        print("\nNenhum jogador cadastrado no banco. Pressione Enter para retornar ao menu.\n")
        input()
        return
    
    db.listar_jogador() #mostra a lista de jogadores
    print("\nDigite 'cancelar' ou '0' para voltar ao menu principal")
    while(True):
        try:
            id = int(input("\nQual o ID do jogador que deseja excluir?\n")) #converte string para int
            if id == 0: #int nao precisa de aspas
                return
            break #sai do loop
        except ValueError:
            os.system('cls')
            print("Digite um valor numérico inteiro ou 0 para voltar ao menu principal.\n")
    if not db.verificar_jogador(id): #se o jogador nao existir
        print(f"\nJogador com ID {id} não encontrado. Pressione Enter para retornar ao menu.\n")
        input() #pausa a tela
        return
    db.excluir_jogador(id)
    opcao = input("\nDeseja excluir outro jogador? (s/n)\n").strip().lower() #remove espacos e coloca em minusculo
    if opcao == 'n':
        return
    elif opcao != 's': #elimina a necessidade de um else --> volta pro loop principal se for diferente de 's' ou 'n'
        print("\nOpção inválida. Por favor, responda com 's' ou 'n'.")


def main():
    db.iniciar_banco()
    while(True): #mantem o menu ativo
        os.system('cls')
        menu()
        opcao = input("\nSelecione uma opção: ")
        match opcao: #switch case
            case "1":
                inserir_jogador()
            case "2":
                listar_jogador()
            case "3":
                listar_jogador_filtro()
            case "4":
                atualizar_jogador()
            case "5":
                excluir_jogador()
            case "6":
                print("Saíndo do menu. Obrigado!")
                db.fechar_banco() #referencia ao banco.py
                sys.exit(0)
            case _: #caso nao escolha um numero do menu
                os.system('cls')
                print("\nOpção Inválida. Por favor, selecione uma das opções exibidas.")
        
main()