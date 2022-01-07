#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print ('Valor do bônus de acordo com o tempo de serviço')
       
anos = int(input('anos de serviço: '))
valor_por_ano = float(input('Valor por ano: '))
bônus = anos * valor_por_ano
print(f'Bônus de R$ {bônus:5.2f}')


# In[ ]:


print ('programa que pede dois números e depois soma eles')
primeiro = int(input('Primeiro número da soma: '))
segundo = int(input('Segundo número da soma: '))
soma = primeiro + segundo
print (f'O total dos dois somados é {soma}')


# In[ ]:


print ('programa que lê em metros e exibe convertido em milimetros:')

metro = int(input("Digite o valor em metros: "))
milimetro = metro * 1000
print (f"{metro} metros é igual a {milimetro} milimetros")


# In[ ]:


print ('Programa que lê a quantidade de dias, horas, minutos e segundos. Vai exibir o total em segundos:')


dias = int(input('Digite a quantidade de dias '))
horas = int(input('Digite a quantidade de horas '))
minutos = int(input('Digite a quantidade de minutos '))
segundos = int(input('Digite a quantidade de segundos'))
total = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
print (f'O total é de {total} segundos')


# In[ ]:


print ('Programa que solicita salário e porcentagem de aumento, e depois mostra o valor do aumento e do novo salário:')

salário = float(input('Digite o salário inicial: '))
aumento = float(input('Digite a porcentagem de aumento (sem o simbolo de %):'))
valor_aumento = (aumento / 100) * salário
novo_salário = valor_aumento + salário
print (f'O aumento vai ser de R${valor_aumento:5.2f}')
print (f'O novo salário vai ser de R${novo_salário:5.2f}')


# In[ ]:


print ('Programa que pede o valor de uma mercadoria e o percentual de desconto e mostra o valor a pagar com desconto')
valor = float(input('Digite o valor normal do produto: '))
desconto = float(input('Digite o percentual de desconto: '))
valor_final = valor - ((desconto / 100) * valor)
print (f'O valor com o desconto é R${valor_final:5.2f}')


# In[ ]:


print ('Programa que solicita a distancia do percurso e a velocidade média de um carro e mostra a duração da viagem')
distancia = float(input('Digite a distancia da viagem: '))
velocidade = float(input('Digite a velocidade média do veículo: '))
duração = (distancia / velocidade) * 60
print (f'A duração vai ser de aproximadamente {duração:.0f} minutos')


# In[ ]:


print ('Programa que converte Celsius em Fahrenheit:')
c = float(input('Insira o valor da temperatura em Celsius (c°): '))
f = float ((9*c) / 5) + 32
print (f'{f} Fahrenheit')


# In[ ]:


print ('Programa que pergunta a ditancia percorrida por um carro alugado e a quantidade de dias que durou o aluguel')
print ('Calcula o preço a pagar sendo que: aluguel é R$60 por dia e R$0,15 por km rodado')


distancia = float(input('Digite a distância total percorrida com o carro: '))
duração = float(input('Digite quantos dias ficou o carro: '))
total = (duração * 60) + (distancia * 0.15)
print (f'O valor a ser pago é de R${total:.2f}')


# In[ ]:


print ('Programa que calcula a redução no tempo de vida de um fumante:')
#1 cigarro = 10 minutos a menos de vida
print()
print()
print ('Quantos  vezes você é imbecil por dia?')
por_dia = int(input('Ops, pergunta errada. Era pra ser: Quantos cigarros você fuma por dia? '))
quanto_tempo = int(input('A quantos anos você fuma? '))
tempo_perdido = por_dia * 365 * 10 * quanto_tempo #quantidade por dia, vezes dias do ano vezes a quantia perdida por cada cigarro
perdido = tempo_perdido / 525960
print (tempo_perdido)
print (f'Você já perdeu {perdido:0.1f} anos de vida!!! Parabéns jeniu!!!')



# In[ ]:




