# Exercício 1: Faça um programa que solicite o nome de uma pessoa usuária e imprima-o na vertical.
# name = input('')
# for letter in name:
#     print(letter)

# Exercício 2: Escreva um programa que receba vários números naturais e calcule a soma desses valores. Caso algum valor da entrada seja inválido (por exemplo uma letra), uma mensagem deve ser exibida na saída de erros no seguinte formato: “Erro ao somar valores, {valor} é um valor inválido”. Ao final, você deve imprimir a soma dos valores válidos.
numbers = input('')

for number in numbers:
    if not number.isdigit():
        raise ValueError('Are not numeric values')
    else:
        sum += int(number)

print(f"A soma dos valores válidos é: {sum}")