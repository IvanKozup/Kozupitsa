list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

half_len_list = round(len(list_players) / 2)

half_1 = list_players[:half_len_list]
half_2 = list_players[half_len_list:]

print(half_1)
print(half_2)
