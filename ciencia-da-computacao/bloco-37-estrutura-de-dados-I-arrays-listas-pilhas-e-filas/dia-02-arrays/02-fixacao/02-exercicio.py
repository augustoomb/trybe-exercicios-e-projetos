# Exercício 2 Em um jogo de baralho, as cartas estão representadas por um array numérico.
# Para iniciar o jogo, devemos embaralhar as cartas. Faremos isto dividindo uma porção de cartas
# em 2 e depois mesclando as duas porções. Por exemplo:

# Exemplo 1:
# cartas = [2, 6, 4, 5]
# cartas por parte = 2

# resultado = [2, 4, 6, 5]

# Exemplo 2:
# cartas = [1, 4, 4, 7, 6, 6]
# cartas por parte = 3

# resultado = [1, 7, 4, 6, 4, 6]


def shuffle_cards(list_cards):    
    middle = len(list_cards) // 2
    sub_arr1 = list_cards[:middle]
    sub_arr2 = list_cards[middle:]

    shuffle_list = []

    for index in range(middle):
        shuffle_list.append(sub_arr1[index])
        shuffle_list.append(sub_arr2[index])

    return shuffle_list

print(shuffle_cards([1, 4, 4, 7, 6, 6]))

# Complexidade O(n)

