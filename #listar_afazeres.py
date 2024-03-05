import sqlite3
conexao = sqlite3.connect('atividade_m2s4.sqlite3')
cursor = conexao.cursor()

print('\nLISTA DE AFAZERES POR DIA ESPECÍFICO')
dia = input('\nQual o dia da semana?: ')

sql = 'select nome_tarefa from tarefa where dia = ?'

consulta = cursor.execute(sql, [dia])

for resultado in consulta:
    print(resultado)