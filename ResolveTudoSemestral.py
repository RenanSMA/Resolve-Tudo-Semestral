# Código criado em 17/02/2025.

# Um professor desenvolveu uma prova abordando os seguintes assunstos: Média, Moda, Mediana, Variância e Desvio Padrão. Foi informado que os alunos poderiam utilizar calculadora na prova. Por sua vez, um aluno perguntou se poderia criar um sistema em Python, o qual solucionária os cálculos necessários. O Professor gostou da ideia e permitiu que se consolidasse. Quem quisesse estava livre para fazer.

# Confira a seguir o código feito pelo aluno.

# Média, Moda, Mediana, Variância, Desvio Padrão


# Solicita ao Usuário o tamanho da lista desejada para calcular
tamanho_lista = int(input("Digite o tamanho da lista dos números que deseja calcular: "))

# Lista Vazia que terá seu tamanho definido pelo Usuário
lista = []

# Solicita os números sequencialmente
for i in range(tamanho_lista):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista.append(numero)

# Exibe a lista preenchida e os números informados sequencialmente pelo Usuário
print("Lista final:", lista)


# MÉDIA: realiza os cálculos necessários para encontrar a Média
total = 0
for i in lista:
    total += i


media = total / tamanho_lista
print(f'A Média é: {media:.2f}')


# MODA: realiza os cálculos necessários para encontrar a Moda

tabela = {}
for j in lista:
    tabela[j] = tabela.get(j, 0) + 1

# print(tabela)

maior_valor = 0
maior_chave = -1
for chave, valor in tabela.items():
    if valor > maior_valor:
        maior_valor = valor
        maior_chave = chave

moda_encontrada = False
for chave, valor in tabela.items():
    if valor == maior_valor:
        if not moda_encontrada:
            print(f'A Moda é: {chave:.2f}', end=' ')
            moda_encontrada = True
        else:
            print(f'{chave}', end=' ')
print()

# MEDIANA: realiza os cálculos necessários para encontrar a Mediana

lista_ordenada = sorted(lista)

valor1 = int(tamanho_lista / 2) - 1
valor2 = int(tamanho_lista / 2)

if tamanho_lista % 2 == 0:
    mediana = (lista_ordenada[valor1] + lista_ordenada[valor2]) / 2
else:
    mediana = lista_ordenada[valor2]

print(f'A Mediana é: {mediana:.2f}')

# VARIÂNCIA: realiza os cálculos necessários para encontrar a Variância
soma_variancia = 0
for i in lista:
    x = (i - media)**2
    soma_variancia += x

variancia = soma_variancia / tamanho_lista
print(f'A Variância é: {variancia:.2f}')

# DESVIO PADRÃO: realiza os cálculos necessários para encontrar o Desvio Padrão
desvio_padrao = variancia**0.5
print(f'O Desvio Padrão é: {desvio_padrao:.2f}')