ATIVIDADE 2 - APE 

QUESTÃO 1:
Escreva um programa para ler uma temperatura
dada na escala Fahrenheit e exibir o equivalente
em Celsius.
 C= 5 
   --- (F-32)
    9 
    
temperatura=float(input('Informe a temperatura em Fahrenheit: '))
cel=(temperatura - 32) * 5/9
print('O valor da temperatura Fahrenheit em Celsius foi: ',cel, '°C')

    
QUESTÃO 2:
[URI – 1012 (Adaptada)] Área.
Escreva um programa que leia três
valores: A, B e C.
Em seguida, calcule e mostre:

a) a área do triângulo retângulo que tem A por base e C por
altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

a=float(input('Valor do lado A: '))
b=float(input('Valor do lado B: '))
c=float(input('Valor do lado C: '))

print('A area do triângulo que tem A por base e C por altura: ',a*c/2)
print('A área do círculo de raio C: ',2*314159*c)
print('A área do trapézio que tem A e B por bases e C por altura: ',(a+b)/2*c) 
print('A área do quadrado que tem lado B: ',b*b)
print('A área do retângulo que tem lados A e B: ',a*b)


QUESTÃO 3:
Uma certa empresa deseja aumentar o salário de seus empregados em 20%.
Escrever um programa que leia o nome e o salário atual de um empregado, e exiba o nome, o salário atual e o salário reajustado.

nome=input('Seu nome: ')
salario=float(input('Seu salário: '))
sr=salario+(salario*20/100)
print('Olá',nome,'seu salario foi R$',salario,' e com um ajuste de 20% seu salario ficou R$',sr)


QUESTÃO 4:
Considerando a lista de produtos e seus respectivos preços abaixo, escreva um programa para ler as quantidades consumidas de cada produto
por um cliente, calcular e exibir o preço total consumido.

Chocolate R$ 4,00
Refrigerante R$ 5,00
Misto Quente R$ 3,50
Sorvete R$ 3,00

c=int(input('Quantos chocolates você consumiu? '))
r=int(input('Quantos refrigerantes você consumiu? '))
m=int(input('Quantos mistos quentes você consumiu? '))
s=int(input('Quantos sorvetes você consumiu? '))
total=c*4+r*5+m*3.5+s*3

print('Voce consumiu',c, 'chocolate(s) e o preço total foi: R$',c*4)
print('Voce consumiu',r, 'refrigerante(s) e o preço total foi: R$',r*5)
print('Voce consumiu',m, 'misto(s) quente(s) e o preço total foi: R$',m*3.5)
print('Voce consumiu',s, 'sorvete(s) e o preço total foi: R$',s*3)
print('E o seu valor total foi de: R$:',total)
