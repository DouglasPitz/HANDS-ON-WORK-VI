from classes import Biblioteca, Livro


def inserir_no_banco_livro(conexao, titulo, autor, ano):
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO livro (titulo, autor, ano_de_publicacao, biblioteca_id) VALUES(%s, %s, %s, %s)",
        (titulo, autor, ano, '1')
    )
    conexao.commit()
    cursor.close()
    conexao.close()


def inserir_no_banco_biblioteca(conexao, nome, endereco):
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO biblioteca (nome, endereco) VALUES(%s, %s)",
        (nome, endereco)
    )
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_bibliotecas(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM biblioteca")
    linhas = cursor.fetchall()

    list = []
    for linha in linhas:
    # appending instances to list
        list.append(Biblioteca(linha[1], linha[2]))

    linhas = list

    cursor.close()
    return linhas



def consultar_livros(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livro")
    linhas = cursor.fetchall()

    list = []
    for linha in linhas:
    # appending instances to list
        livro = Livro(linha[0], linha[1], linha[2], linha[3], linha[7])

        list.append(livro)


    cursor.close()
    conexao.close()
    return list


def randon_biblioteca_id(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM biblioteca")
    linhas = cursor.fetchall()