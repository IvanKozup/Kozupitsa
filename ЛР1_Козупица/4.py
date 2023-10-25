users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

visiting_list = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

length = len(users)
unique_length = len(set(users))

visiting_list["Общее количество"] = length
visiting_list["Уникальные посещения"] = unique_length

print(visiting_list)
