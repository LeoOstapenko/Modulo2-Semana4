import sqlite3

conexao = sqlite3.connect('atividade_m2s4.sqlite3')

print('\nCRIAÇÃO DE NOVA TAREFA')
nome = input('\nNOME NOVA TAREFA --> ')
categoria = int(input('CATEGORIA TAREFA --> '))
dia = input('DIA PARA REALIZAÇÃO DA TAREFA --> ')
valores = [nome, categoria, dia]

sql_criacao = 'insert into tarefa (nome_tarefa, categoria_id, dia, conclusao) values (?, ?, ?, "Não")'

cursor = conexao.cursor()

cursor.execute(sql_criacao, valores)

conexao.commit()
conexao.close()