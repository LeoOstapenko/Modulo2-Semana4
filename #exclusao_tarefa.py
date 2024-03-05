import sqlite3
conexao = sqlite3.connect('atividade_m2s4.sqlite3')

cursor = conexao.cursor()

print('\nAÇÃO DE EXCLUSÃO DE TAREFA')

id = int(input('\nEXCLUIR TAREFA COM O ID --> '))

sql_excluir = 'DELETE FROM tarefa WHERE id = ?'

valores = [id]
cursor.execute(sql_excluir, valores)

conexao.commit()
conexao.close()