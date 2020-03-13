1.Escreva um programa que leia um número inteiro e determine se ele é par ou ímpar

n1=int(input('informe um numero: '))
valor=n1%2

if valor==0:
    print('O número é par')
else:
    print('O número é impar')

--

2.Escreva um programa que leia dois números e exiba-os em ordem crescente.

n1=int(input('Informe o primeiro numero: '))
n2=int(input('Informe o segundo numero: '))

if n1>n2:
  print(n2,n1)
else:
  print(n1,n2)

--

3.Escreva um programa que leia 3 números inteiros, determine e mostre o maior deles.

n1=int(input('Informe o primeiro número: '))
n2=int(input('Informe o segundo número: '))
n3=int(input('Informe o terceiro número: '))

if n1>n2 and n1>n3:
  print('O maior número foi', n1)
if n2>n1 and n2>n3:
  print('O maior número foi', n2)
if n3>n1 and n3>n2:
  print('O maior número foi o', n3)
  
--

4.Escreva um programa que leia o nome e o sexo (M ou F) de uma pessoa e exiba a mensagem 
"Olá, Sr. Fulano!" ou "Olá, Sra. Fulana!", de acordo com o sexo da pessoa.
Obs: Fulano e Fulana são nomes exemplos.

nome=input('Informe seu nome: ')
sexo=input('Informe seu sexo [M/F]: ')

if sexo == 'M':
    print('Olá, Sr.',nome)
if sexo == 'F':
     print('Olá, Sra.',nome)
     
--
    
5.A empresa Vende Tudo Ltda paga o salário de cada vendedor com uma comissão de 5% sobre o total
de vendas daquele vendedor, mas essa comissão nunca deve ser inferior ao salário mínimo.
Escreva um algoritmo que leia o valor total das vendas de um vendedor e escreva seu salário. 


6.Escreva um programa para  determinar  as  raízes  de  uma  equação  de  segundo  grau,  dados  os 
seus coeficientes.
Fórmulas: 
Obs: se Δ for negativo, não existem as raízes da equação. Dica: use a função sqrt do módulo math.


7.Escreva um programa que tenha a funcionalidade de uma calculadora simples.
O programa deve solicitar a digitação de dois operandos e um operador (+ - x * / %)
e deve imprimir ao resultado da operação aritmética.
Caso o usuário digite um operador inválido, o programa deve imprimir "Operador desconhecido".

n1=int(input('Informe o primeiro operando: '))
n2=int(input('Informe o segundo operador: '))
op=str(input('Informe o operador: '))
if op=='+':
	print(n1+n2)
elif op=='-':
	print(n1-n2) 
elif op=='*':
	print(n1*n2)
elif op=='/':
	print(n1//n2)
elif op=='%':
	x=n1/100
	z=x*n2
	y=z
	print(y)
else: 
    print('Operador desconhecido')
    
--

8.Escreva um programa que solicite a digitação de um número (de 1 a 7) correspondente a um dia da semana
e imprima o nome do dia da semana e se é dia útil (de segunda a sexta) ou final de semana
(sábado e domingo). Considere que o dia 1 é o domingo.

dia=int(input('Informe um numero (de 1 a 7): '))
if dia =='1':
    print('Hoje é domingo. Fim de semana. ')
if dia =='2':
    print('Hoje é segunda. Dia útil. ')
if dia =='3':
    print('Hoje é terça. Dia útil. ')
if dia =='4':
    print('Hoje é quarta. Dia útil. ')
if dia =='5':
    print('Hoje é quinta. Dia útil. ')
if dia =='6':
    print('Hoje é sexta. Dia útil. ')
if dia =='7':
    print('Hoje é sábado. Fim de semana. ') # sem aspas

--

9.Escreva um programa que solicite a digitação de um caractere qualquer do teclado e imprima 
sua classificação: vogal, consoante, número e caractere especial. 
	
	
c=input('Digite qualquer coisa: ')
if c=='@' or c== '!' or c== '$' or c=='#' or c== '%' or c== '=' or c== '&' or c== '(' or c=='*' or c== '+' or c== '/':
    print('Caractere especial ')
elif c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
    print('Vogal')
elif for i in range(10, -1, -1):
    print('numero')


--

10.Escreva  um  programa  que  leia  a  idade  de  um  nadador  e  classifique-o em  sua
respectiva categoria, de acordo com a tabela abaixo:
	
	IDADE CATEGORIA5
	5 a 10 anos Infantil
	11 a 17 anos Juvenil
	18 a 49 anos Adulto
	50 anos ou mais Senior
	
id=int(input('Informe sua idade: '))
if id >=5 and id <=10:
	print('Infantil')
if id >=11 and id <=17:
	print('Juvenil ')
if id>=18 and id <=49:
	print('Adulto')
else:
	print('Senior')
	
--

11.Escreva um programa que leia o peso e a altura de uma pessoa, determine e mostre
o seu grau de obesidade, de acordo com a tabela seguinte.
O grau de obesidade é determinado pelo índice de massa corpórea,
cujo cálculo é realizado dividindo-se o peso da pessoa pelo quadrado da sua altura.

peso=float(input('Informe seu peso: '))
alt=float(input('Informe sua altura: '))
x=peso/alt*2
if x<26:
    print('Normal')
elif x>=26 and x<30:
    print('Obeso')
else:
    print('Obeso Mórbido')
    
--

12.Um  banco  concederá  um  crédito  especial  aos  seus  clientes,  de  acordo  com  o  saldo  médio
de cada cliente no último ano. Escreva um programa que leia o nome e o saldo médio de um cliente
e calcule o valor do créditode acordo com a tabela abaixo. 

		SALDO MÉDIO  		(R$)PERCENTUAL
		de 0 a 500 		Nenhum crédito
		acima de 500 até 1.000 - 20% do valor do saldo médio
		acima de 1.000 até 2.500 - 30% do valor do saldo médio 
		acima de 2.500 		40% do valor do saldo médio
	
nome=input('Digite seu nome: ')
saldo=int(input('Digite seu saldo médio: '))
if saldo>=0 and saldo<=500:
    print('Olá,',nome, 'nenhum saldo')
elif saldo >=500 and saldo<=1000:
    print(f'Olá {nome} seu saldo é de {saldo*2.0*2}')
elif saldo>=1000 and saldo <=2500:
    print('Olá',nome, 'seu saldo é de',saldo*0.3)
else:
    print('Olá',nome,' seu saldo é de' ,saldo*0.4)


--

13.Escreva um programa que leia quatro notas e calcule a média obtida, desprezando a nota mais baixa. 
O programa deverá determinar o conceito do aluno na disciplina, de acordo com a tabela seguinte:
	MÉDIA 		CONCEITO
	9,0		 A
	7,5 e < 9,0	 B
	6,0 e < 7,5	 C
	4,0 e < 6,0	 D
	< 4,0		 E
	
	
n1=float(input('Informe sua primeira nota: '))
n2=float(input('Informe sua segunda nota: '))
n3=float(input('Informe sua terceira nota: '))
n4=float(input('Informe sua quarta nota: '))

media = (n1+n2+n3+n4)/3
if (n1<n2) and (n1<n3) and (n1<n4):
    if media>=9.0:
        print('A sua media foi',media, 'seu conceito foi A. APROVADO')
elif (n2<n1) and (n2<n3) and (n2<n4):
    if media>=7.5 and media <9.0:
        print('A sua media foi',media, 'seu conceito foi B. APROVADO')
elif (n3<n2) and (n3<n1) and (n3<n4):
    if media >=6.0 and media <7.5:
        print('A sua media foi',media,  'seu conceito foi C. APROVADO')
elif (n4<n1) and (n4<n2) and (n4<n3):
    if media >=4.0 and media <6.0:
        print('A sua media foi',media, 'SEU CONCEITO FOI D. REPROVADO')
else: 
    print('Seu conceito foi E. REPROVADO. ')

--

14.Na primeira etapa de umconcurso, o candidato tem que fazer duas provas.
Dessas duas notas é tirada a média do candidato. Caso essa média seja maior ou igual a 7.0,
ele estará apto a fazer a segunda etapa do concurso.
Na segunda etapa, ele fará mais uma prova, onde deverá obter uma nota maior ou igual a 8.0
para ser aprovado no concurso. 
Escreva um programa que leia as notas da primeira etapa, calcule a média da primeira etapa, 
e se o candidato for aprovado na primeira etapa, leia a nota dele na segunda etapa e diga se 
ele foi aprovado ou não no concurso.

n1=float(input('Olá candidato(a) informe sua primeira nota: '))
n2=float(input('Informe sua segunda nota: '))
media=(n1+n2)/2
if media>=7.0:
    print('Você está apto para participar da segunda etapa. ')
else:
    print('Você não está apto a participar da segunda etapa do concurso. ')
seg=float(input('Informe sua nota na segunda etapa: '))
if seg>=8.0:
    print('Você foi aprovado no concurso. ')

--


15.Escreva um programa que leia a hora de início de um jogo e a hora do final do jogo
(considerando apenas horas inteiras), calcula a duração do jogo em horas, 
sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar 
em um dia e terminar no dia seguinte. O programa deve mostrar o resultado obtido.


16.Escreva  um programa que  solicite  a  digitação  de  um  ano  e  imprima  sua  classificação
comobissexto ou não bissexto. Obs: um ano é bissexto se for divisível por 4, mas não por 100. 
Um ano também é bissextose for divisível por 400. 

17.Escreva um programa para calcular a conta final de um hóspede de um hotel, considerando que:
	
a)Serão lidos o nome do hóspede, o tipo do apartamento utilizado (A, B, C ou D),
o número de diárias utilizadas pelo hóspede e o valor do consumo interno do hóspede;

b)O valor da diária é determinado pela seguinte tabela:
	
	 TIPO DO APTO   		VALOR DA DIÁRIA
		A			R$150,00
		B			R$100,00
		C			R$75,00
		D			R$50,00
		
	
c)O valor total das diárias é calculado pela multiplicação do número de diárias utilizadas pelo valor
da diária;

d)O subtotal é calculado pela soma do valor total das diárias e o valor do consumo interno;

e)O valor da taxa deserviço equivale a 10% do subtotal;

f)O total geral resulta da soma do subtotal com a taxa de serviço. 

O programa deverá mostrar a conta final do hóspede, contendo: o nome do hóspede,
o tipo do apartamento, o número de diárias utilizadas, o valor unitário da diária,
o valor total das diárias, o valor do consumo interno, o subtotal, o valor da taxa de 
serviço e o total geral.




	
	
	
	
	
	
	
	
	
	
	
	
	
