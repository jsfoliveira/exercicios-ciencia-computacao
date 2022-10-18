# $python3
# a identação são 4 casas
# não usa switch case em python
# condicional
patheon = [
  {"nome": "Wynna", "domínio": "Magia"},
  {"nome": "Nimb", "domínio": "Sorte"},
  {"nome": "Ahadarak", "domínio": "Tormenta"},
]

# importando a biblioteca random
from random import randint;
dice_roll = randint(1,20)
if dice_roll == 1:
    print("Deu ruim")
elif 2 <= dice_roll <=15:
    print("Porque me atormenta")
elif 16 <= dice_roll <= 19:
    print("Obrigada pela sorte")
else:
    print("Agora ninguém segura")

salary = 5000
if salary <= 2000:
    print("pessoa desenvolvedora estagiária")
elif 2000 < salary <= 5800:
    print("pessoa desenvolvedora júnior")
elif 5800 < salary <= 7500:
    print("pessoa desenvolvedora pleno")
elif 7500 < salary <= 10500:
    print("pessoa desenvolvedora sênior")
else:
    print("liderança")
