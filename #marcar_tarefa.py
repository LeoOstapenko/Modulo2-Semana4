import sqlite3
conexao = sqlite3.connect('atividade_m2s4.sqlite3')

cursor = conexao.cursor()

print('\n# TICAR CONCLUSÃO DE TAREFA #')

id = int(input('\nDIGITE O ID DA TAREFA CONCLUÍDA --> '))

sql_atualiza = 'UPDATE tarefa SET conclusao = "Sim" WHERE id = ?'

valores = [id]
cursor.execute(sql_atualiza, valores)

conexao.commit()
conexao.close()