# enumerate
# Em Python, um loop for geralmente é escrito como um loop sobre um objeto iterável. Isso significa que você não precisa de uma variável de contagem para acessar itens no iterável.
languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

# converte um objeto enumerate em uma lista
print(list(enumerate_prime))

# Saída: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

# While
n = 10
last, next = 0, 1
while last < n:
    print(last)
    last, next = next, last + next

# Exercício 12
# O Fatorial de um número inteiro é representado pela multiplicação de todos os números predecessores maiores que 0. Por exemplo, o fatorial de 5 é 120 pois 5! = 1 * 2 * 3 * 4 * 5. Escreva um código que calcule o fatorial de um número inteiro.


# Exercício 13
# Um sistema de avaliações registra valores de 0 a 10 para cada avaliação. Após algumas mudanças estes valores precisam ser ajustados para avaliações de 0 a 100. Dado uma sequência de avaliações ratings = [6, 8, 5, 9, 10]. Escreva um código capaz de gerar as avaliações após a mudança. Neste caso o resultado deveria ser [60, 80, 50, 90, 100].
ratings = [6, 8, 5, 9, 10]
new_ratings = []
for score in ratings:
    new_ratings.append(ratings*10)

# Exercício 14
# Percorra a lista do exercício 13 e imprima “Múltiplo de 3” se o elemento for divisível por 3.
for multiply in new_ratings:
    if (multiply % 3) == 0:
        print(f'{multiply} é múltiplo de 3')
