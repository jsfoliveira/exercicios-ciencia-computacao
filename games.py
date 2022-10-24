import json

# with diz que dentro desse contexto, o arquivo vai ser só lido; fora dele, muda, não precisa abrir e fechar o arquivo sempre
# python3 -i games.py
try:
    with open('games.json', 'r') as file:
        video_game = json.load(file)
except FileNotFoundError as exec:
    print("arquivo não encontrado")


all_consoles = set()

for game in video_game:
    console = game['Release']['Console']
    all_consoles.add(console)


all_genres = set()
score_by_genre = {genre: [] for genre in all_genres}

avg_score_by_genre = {}
for genre, scores in scores_by_genre.items():
    avg_score_by_genre[genre] = sum(scores) / len(scores)

print(f"Média: {avg_score_by_genre}")
