import sqlite3
conexao = sqlite3.connect('atividade_m2s4.sqlite3')

cursor = conexao.cursor()

print('\nAÇÃO DE EXCLUSÃO DE CATEGORIA')

id = int(input('\nEXCLUIR CATEGORIA COM O ID --> '))

sql_excluir = 'DELETE FROM categoria WHERE id = ?'

valores = [id]
cursor.execute(sql_excluir, valores)

conexao.commit()
conexao.close()