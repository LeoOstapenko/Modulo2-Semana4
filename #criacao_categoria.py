import sqlite3

conexao = sqlite3.connect('atividade_m2s4.sqlite3')

print('\nCRIAÇÃO DE NOVA CATEGORIA')
nome = input('\nNOME NOVA CATEGORIA --> ')
valores = [nome]

sql_criacao = 'insert into categoria (nome_categoria) values (?)'

cursor = conexao.cursor()

cursor.execute(sql_criacao, valores)

conexao.commit()
conexao.close()