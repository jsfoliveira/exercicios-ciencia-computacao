# 🚀 Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
def twoNumber(a, b):
    if a > b:
        return a
    else:
        return b

twoNumber(2,4)
# 🚀 Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def mediaAritmetica(list):
    soma = sum(list)
    lengthArray = len(list)
    media = soma / lengthArray
    return media

mediaAritmetica([1,2,3])

# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1, imprima na tela um quadrado feito de asteriscos de lado de tamanho n. Por exemplo:
# 🦜Dica: Python sabe multiplicar sequências! Por exemplo, 3 * 'bla' resulta em blablabla. Isso se aplica a listas também, caso você precise.
# Sentiu aí um certo dejavu? 😁
def draw_square(n):
    for row in range(n):
        print(n * '*')
draw_square(10)

# 🚀 Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"], o retorno deve ser "Fernanda".
# 🦜 Uma dica: Utilize a função len() para verificar o tamanho do nome.
def maiorNome(listName):
    biggest_name = listName[0]
    for name in listName:
      if len(name) > len(biggest_name):
        biggest_name = name
    return biggest_name

maiorNome(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"])

# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede (em m²).
def paint_costs(area):
    can_price = 80
    required_liters = area / 3
    required_cans = required_liters // 18
    if required_liters % 18:
        required_cans += 1
    return required_cans, required_cans * can_price

paint_costs(100)


# Exercício 6: Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo formado ou "não é triangulo", caso não seja possível formar um triângulo.
def triangleType(a,b,c):
    if a == b == c:
        print('é triângulo equilátero')
    elif a == b != c:
        print('é triângulo isóceles')
    elif a != b != c:
        print('é triângulo escaleno')
    else:
        print('não é triângulo')

triangleType(2,2,3)