# python3
frutas = ['Abacaxi', 'Morango', 'Uva']
for fruta in frutas:
    print(fruta)
# Resultado
# Abacaxi
# Morango
# Uva

for numero in range(10):
    if numero % 2 == 0:
        print("O número", numero, "é par")
'''
Resultado:
O número 0 é par
O número 2 é par
O número 4 é par
O número 6 é par
O número 8 é par
'''

restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]
filtered_restaurants = []
min_rating = 3.0
for restaurant in restaurants:
    if restaurant["nota"] > min_rating:
        filtered_restaurants.append(restaurant)
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D
# ou pode fazer a lógica dentro do array(compreensão de lista)
min_rating = 3.0
filtered_restaurants = [restaurant
                         for restaurant in restaurants
                         if restaurant["nota"] > min_rating]
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D

# A seguinte cria uma nova lista de strings com os nomes que contém a letra ‘a’.
names_list = ['Duda', 'Rafa', 'Cris', 'Yuri']
new_names_list = [name for name in names_list if 'a' in name]

# Aqui o for percorre cada nome em "names_list", verifica se existe a letra "a" nele,
# o adiciona à variável "name", e então gera nossa nova lista "new_names_list"
print(new_names_list)

# Saída
['Duda', 'Rafa']
# O exemplo a seguir usa uma compreensão de listas para criar uma lista com o quadrado dos números entre 1 e 10.
quadrados = [x*x for x in range(11)]
print(quadrados)

# Saída
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]