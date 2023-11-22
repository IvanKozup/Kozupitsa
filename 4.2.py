# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    with open(INPUT_FILENAME) as csv_file:
        from_csv = csv.DictReader(csv_file, delimiter=",", quotechar="\n")
        to_json = list(from_csv)
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(to_json, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
