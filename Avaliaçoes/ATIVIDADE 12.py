1. Uma certa empresa deseja criar logins para os seus empregados com base na seguinte regra: O primeiro nome seguido pelas iniciais dos sobrenomes (tudo em letras minúsculas). Por exemplo, se o nome for “Carlos Alberto Barbosa Costa”, o login será “carlosabc”. Com base nessa informação, escreva um programa que leia um nome de uma pessoa e gere um login automático para essa pessoa.

nome=input('Informe seu nome completo: ').lower()
div=nome.split()
nome=len(div)
fim=div[0]

for i in range(1, nome):
    fim = fim + div [i][0]

print(fim) 


2. Escreva um programa que, a partir da digitação do infinitivo de um verbo regular, faça a conjugação do mesmo no presente do indicativo para as pessoas do singular e plural.
Exemplo:
Entrada:
CANTAR
Saída:
Eu canto
Tu cantas
Ele canta
Nós cantamos
Vós cantais
Eles cantam

v = input('Qual verbo deseja conjugar? ')
v = v.lower()
t = len(v)
r = v[:t-2]
pe = ['Eu','Tu','Ele','Nós','Vós','Eles']
ar = ['o','as','a','amos','ais','am']
ir = ['o','es','e','imos','is','em']
er = ['o','es','e','emos','eis','em']

for i in range(6):
        if v[-2] == 'a':
            print(pe[i], r + ar[i])
        elif v[-2] == 'e':
            print(pe[i], r + er[i])
        elif v[-2] == 'i':
            print(pe[i], r + ir[i])
