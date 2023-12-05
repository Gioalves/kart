def melhor_volta(matriz):
    melhor_tempo = float('inf')
    volta = 0
    piloto = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < melhor_tempo:
                melhor_tempo = matriz[i][j]
                volta = j + 1
                piloto = i + 1
    return piloto, volta

def classificacao_final(matriz):
    tempos_finais = []
    for i in range(len(matriz)):
        tempo_total = sum(matriz[i])
        tempos_finais.append((i + 1, tempo_total))
    tempos_finais.sort(key=lambda x: x[1])
    return tempos_finais

def volta_media_rapida(matriz):
    voltas_medias = []
    for j in range(len(matriz[0])):
        soma_tempos = 0
        for i in range(len(matriz)):
            soma_tempos += matriz[i][j]
        media_tempo = soma_tempos / len(matriz)
        voltas_medias.append((j + 1, media_tempo))
    voltas_medias.sort(key=lambda x: x[1])
    return voltas_medias[-1][0], voltas_medias[-1][1]

# Leitura dos tempos de cada volta de cada corredor
num_corredores = 6
num_voltas = 10
matriz_tempos = []
for i in range(num_corredores):
    tempos = []
    print(f"Digite os tempos do corredor {i + 1}:")
    for j in range(num_voltas):
        tempo = float(input(f"Volta {j + 1}: "))
        tempos.append(tempo)
    matriz_tempos.append(tempos)

# a) Melhor volta da prova
piloto, volta = melhor_volta(matriz_tempos)
print(f"A melhor volta da prova foi do corredor {piloto} na volta {volta}.")

# b) Classificação final
classificacao = classificacao_final(matriz_tempos)
print("Classificação final:")
for i, tempo in enumerate(classificacao):
    print(f"{i + 1}º lugar: Corredor {tempo[0]} - {tempo[1]} segundos")

# c) Volta com a média mais rápida
volta_media, media_tempo = volta_media_rapida(matriz_tempos)
print(f"\nA volta com a média mais rápida foi a volta {volta_media} com tempo médio de {media_tempo} segundos.")