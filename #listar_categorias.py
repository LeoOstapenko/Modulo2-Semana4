import sqlite3
conexao = sqlite3.connect('atividade_m2s4.sqlite3')
cursor = conexao.cursor()

print('\nLISTA DE CATEGORIAS\n')

sql = 'select nome_categoria from categoria'

consulta = cursor.execute(sql)

for resultado in consulta:
    print(resultado)