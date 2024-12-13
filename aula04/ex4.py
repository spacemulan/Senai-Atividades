#Crie um programa que declare duas variáveis de string, primeiro_nome e
#ultimo_nome, atribua valores a elas, e depois concatene essas strings em uma variável
#nome_completo. Exiba o valor de nome_completo.

primeiro_nome = input('Qual o seu primeiro nome: ')
ultimo_nome = input('Qual o seu ultimo nome:')
nome_completo = primeiro_nome + ' ' + ultimo_nome
print(f'Nome completo: {nome_completo}')