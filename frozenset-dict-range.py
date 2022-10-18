# $python3
# a variável set é mutável e a frozenset é imutável
permissions = frozenset(["member", "group"])  # assim como o set, qualquer estrutura iterável pode ser utilizada para criar um frozenset

permissions.union({"user"})  # novos conjuntos imutáveis podem ser criados à partir do original, mas o mesmo não pode ser modificado

permissions.intersection({"user", "member"})  # retorna um conjunto resultante da intersecção dos conjuntos

permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos

# Dicionários (dict)
# Estrutura que associa uma chave a um determinado valor. É a representação do tão famoso objeto que utilizamos em JavaScript.
people_by_id = {1: "Maria", 2: "Fernanda", 3: "Felipe"}  # elementos no formato "chave: valor" separados por vírgula, envolvidos por chaves

people_by_name = {"Maria": 1, "Fernanda": 2, "Felipe": 3}  # outro exemplo, dessa vez usando strings como chaves. As aspas são necessárias para que o Python não ache que `Maria`, `Fernanda` e `Felipe` sejam variáveis.

# elementos são acessados por suas chaves
people_by_id[1]  # saída: Maria

# elementos podem ser removidos com a palavra chave del
del people_by_id[1]
people_by_id.items()  # dict_items([(1, "Maria"), (2, "Fernanda"), (3, "Felipe")])
# um conjunto é retornado com tuplas contendo chaves e valores

info = {
  "personagem": "Margarida",
  "origem": "Pato Donald",
  "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}
# Exercício 8: Insira no objeto uma nova propriedade com o nome de chave “recorrente” e o valor “Sim”. Em seguida, imprima o objeto no console.
info["recorrente"] = "Sim"
# Exercício 9: Remova a propriedade cuja chave é “origem” e imprima o objeto no console.
del info["origem"]


# Range (rvariar)
# Estrutura capaz de gerar uma sequência numérica de um valor inicial até um valor final, modificando seu valor de acordo com o passo (step) definido. Pode ser declarado como range( [start], stop[, step] ), em que start e step podem ser omitidos, possuindo valores iniciais iguais a 0 e 1 respectivamente.

# range(início, parada, incremento)
#início: é um valor opcional e corresponde a partir de qual número o range será iniciado;
# parada: é um valor obrigatório e indica o número de parada do range;
# incremento: é opcional e indica o valor que queremos adicionar entre um item e outro.

# Anota aí ✏️: O stop não é incluído na sequência, portanto, caso queira uma sequência de 1 até 10 a chamada deverá ser range(1, 11)
# Seus valores são criados à medida que esta sequência é percorrida.
# vamos converter o range em uma lista para ajudar na visualização

# definimos somente o valor de parada
list(range(5))  # saída: [0, 1, 2, 3, 4]

# definimos o valor inicial e o de parada
list(range(1, 6))  # saída: [1, 2, 3, 4, 5]

# definimos valor inicial, de parada e modificamos o passo para 2
list(range(1, 11, 2))  # saída: [1, 3, 5, 7, 9]

# podemos utilizar valores negativos para as entradas também
list(range(10, 0, -1))  # saída: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Exercício 10: Após uma consulta do banco de dados, temos linhas que contém nome, sobrenome e idade como: "Thiago", "Nobre", 29. Que estrutura vista anteriormente seria recomendada dado que após esta consulta somente exibimos estes valores?
people = {"name": "Thiago", "lastname": "Nobre", "age": 29}
people["age"]

# Exercício 11: Realizar a contagem de quantas vezes cada elemento aparece em uma sequência é uma técnica muito útil na solução de alguns problemas. Qual é a estrutura mais recomendada para o armazenamento desta contagem?
my_list = [20, 20, 1, 2];
count_elements = {
    20: 2,
    1: 1,
    2: 2
}
