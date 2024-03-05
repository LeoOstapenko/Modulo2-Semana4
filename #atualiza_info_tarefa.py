import sqlite3
conexao = sqlite3.connect('atividade_m2s4.sqlite3')

cursor = conexao.cursor()

print('\n# ATUALIZAR INFORMAÇÕES DE TAREFA #')

id = int(input('\nID TAREFA --> '))
nome = input('\nNOME TAREFA --> ')
categoria = int(input('CATEGORIA TAREFA --> '))
dia = input('DIA PARA REALIZAÇÃO DA TAREFA --> ')
conclusao = input('FOI CONCLUÍDA? Sim/Não? --> ')

sql_atualiza = 'UPDATE tarefa SET nome_tarefa = ?, categoria_id = ?, dia = ?, conclusao = ? WHERE id = ?'

valores = [nome, categoria, dia, conclusao, id]
cursor.execute(sql_atualiza, valores)

conexao.commit()
conexao.close()