import sqlite3
import os

conexao = sqlite3.connect("banco.db") #conectar banco
cursor = conexao.cursor()

def iniciar_banco(): #cria a tabela se nao existir --> IF NOT
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS squad( 
                    id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                    nome TEXT UNIQUE NOT NULL,
                    idade INTEGER NOT NULL,
                    time TEXT NOT NULL,
                    posicao VARCHAR(3),
                    nacionalidade TEXT NOT NULL
                   )
                """)

#verificar jogador existente
def verificar_jogador(id):
    cursor.execute("SELECT * FROM squad WHERE id = ?", (id,)) #sqlite3 tem problema com id pq pega o valor como numero (5) = 5 --> colocar virgula no final
    jogador = cursor.fetchone() #pega o primeiro resultado
    if jogador: #se existir
        return True #usa pra mensagem de sucesso no main.py
    else: #se nao existir
        return False #usa pra mensagem de erro no main.py

#verificar banco vazio
def verificar_banco_vazio():
    cursor.execute("SELECT COUNT(*) FROM squad")
    count = cursor.fetchone()[0] #[0] pq fetchone retorna uma tupla --> (count,)
    if count == 0: #vazio?
        return True #volta True
    else: #tem item?
       return False #volta False

#CRUD - Create, Read, Update, Delete

#Create
def inserir_jogador(nome, idade, time, posicao, nacionalidade):
    try:
        cursor.execute("INSERT INTO squad (nome, idade, time, posicao, nacionalidade) VALUES (?, ?, ?, ?, ?)",
                       (nome, idade, time, posicao, nacionalidade))
        conexao.commit() #salva as alteracoes
        print("Jogador adionado ao banco com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Jogador já existente no banco.")
##
#Read
def listar_jogador():
    cursor.execute("SELECT * FROM squad")
    jogador = cursor.fetchall() #lista
    for j in jogador:
        os.system('cls')
        # print("\n")
        print(j) #nao precisa de j++

# def listar_jogador_id:

# def listar_jogador_nome:

# def listar_jogador_time:

# def listar_jogador_posicao:

# def listar_jogador_nacionalidade:


##
#Update
def atualizar_jogador(id, nome, idade, time, posicao, nacionalidade):
    cursor.execute("""
                   UPDATE squad SET nome = ?, idade = ?, time = ?, posicao = ?, nacionalidade = ?
                   WHERE id = ?""", 
                   (nome, idade, time, posicao, nacionalidade, id))
    if cursor.rowcount > 0: #se a linha for atualizada
        return True
    else:
        return False


#Delete
def excluir_jogador(id):
    cursor.execute("DELETE FROM squad WHERE id = ?", (id,)) #sqlite3 tem problema com id pq pega o valor como numero (5) = 5 --> colocar virgula no final
    if cursor.rowcount > 0: #se a linha for excluida
        print("Jogador excluído com sucesso!")
        conexao.commit() #salva as alteracoes
    else:
        print("Erro: Jogador não encontrado.")


#Fechar conexao
def fechar_banco():
    conexao.commit()
    conexao.close()