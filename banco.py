import sqlite3

conexao = sqlite3.connect("banco.db") #conectar banco
cursor = conexao.cursor()

#criar tabela
#ideia futura - talvez adicionar peso e altura? tem que converter valores metro -> cm ou kg -> lb
def criar_tabela():
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS squad(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    time TEXT NOT NULL,
                    posicao VARCHAR(3),
                    nacionalidade TEXT NOT NULL
                   )
                """)

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

#Read
def listar_jogador():
    cursor.execute("SELECT * FROM squad")
    jogador = cursor.fetchall() #lista
    for j in jogador:
        print(j) #nao precisa de j++

#Update
def atualizar_jogador(id, new_nome, new_idade, new_time, new_posicao, new_nacionalidade):
    cursor.execute("""
                   UPDATE squad SET nome = ?, idade = ?, time = ? posicao = ?, nacionalidade = ?
                   WHERE id = ?""", 
                   (new_nome, new_idade, new_time, new_posicao, new_nacionalidade, id))
    if cursor.rowcount > 0: #se a linha for atualizada
        print("Jogador atualizado com sucesso!")
        conexao.commit() #salva as alteracoes
    else:
        print("Jogador não encontrado.")

#Delete
def excluir_jogador(id):
    cursor.execute("DELETE FROM squad WHERE id = ?", (id))
    if cursor.rowcount > 0: #se a linha for excluida
        print("Jogdor excluído com sucesso!")
        conexao.commit() #salva as alteracoes
    else:
        print("Erro: Jogador não encontrado.")

#Fechar conexao
def fehcar_banco():
    conexao.commit()
    conexao.close()