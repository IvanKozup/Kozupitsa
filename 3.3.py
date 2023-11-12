# TODO  Напишите функцию count_letters
def count_letters(text):
    split_small_text = text.lower().split()
    join_text = "".join(split_small_text)
    letters_in_text = {}
    for letter in join_text:
        if letter.isalpha():
            if letter in letters_in_text:
                letters_in_text[letter] += 1
            else:
                letters_in_text[letter] = 1
    return letters_in_text

# TODO Напишите функцию calculate_frequency

def calculate_frequency(dict_letters):
    sum_up = sum(dict_letters.values())
    dict_frequency = {}
    for letter in dict_letters:
        dict_frequency[letter] = dict_letters[letter] / sum_up
    return dict_frequency




main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
count = count_letters(main_str)
frequency = calculate_frequency(count)
for index, letter in enumerate(frequency):
    print(f"{letter}: {frequency[letter]:.2f}")
