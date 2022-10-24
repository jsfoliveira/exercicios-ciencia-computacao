import csv

# try:
#     with open(caminho_do_arquivo , r) as file:
#     arquivo_csv = csv.reader(file)
# except FileNotFoundError as exc:
#     print("O arquivo não foi encontrado")

with open(caminho_do_arquivo , r) as file:
     arquivo_csv = csv.reader(file)

     for linha in arquivo_csv:
         print(linha)

