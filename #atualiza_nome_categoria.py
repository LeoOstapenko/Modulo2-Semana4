import sqlite3
conexao = sqlite3.connect('atividade_m2s4.sqlite3')

cursor = conexao.cursor()

print('\n# ATUALIZAR NOME DA CATEGORIA #')

id = int(input('\nALTERAR NOME DA CATEGORIA DE ID --> '))
nome = input('\nNOVO NOME CATEGORIA --> ')

sql_atualiza = 'UPDATE categoria SET nome_categoria = ? WHERE id = ?'

valores = [nome, id]
cursor.execute(sql_atualiza, valores)

conexao.commit()
conexao.close()