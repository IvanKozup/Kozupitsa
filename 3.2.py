# TODO Напишите функцию find_common_participants
def find_common_participants(participants_1, participants_2, arg=","):
    participants_1_2 = set(participants_1.split(arg)).intersection(set(participants_2.split(arg)))
    participants_1_2_list = list(participants_1_2)
    participants_1_2_list.sort()
    return participants_1_2_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, "|"))
