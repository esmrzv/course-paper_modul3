import json
import operator
import datetime
from os.path import dirname, join

ROOT_DIR = dirname(dirname(__file__))
print(ROOT_DIR)
json_file_path = join(ROOT_DIR,'operation.json')


def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filtered_file():
    data_file = load_file(ROOT_DIR)
    filtered_data = [item for item in data_file if item.get('date') is not None]
    return filtered_data


def sorted_file():
    filtered_data = filtered_file()
    data_sorted = sorted(filtered_data, key=operator.itemgetter('date'), reverse=True)
    list_executed_operation = []
    count = 0
    for operation in data_sorted:
        if operation['state'] == "EXECUTED":
            count += 1
            list_executed_operation.append(operation)
            if count == 5:
                return list_executed_operation


def format_date(date_str):
    date_str = date_str.replace("T", ' ')
    date_obj = datetime.datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")


def mask_card_number(card_number):
    if card_number[0] == 'V':
        masked_number = card_number[:12] + " " + card_number[13:17] + " ******** " + card_number[25:29]
    elif card_number[0] == 'С':
        masked_number = card_number[:4] + ' ' + '**' + card_number[21:25]
    else:
        masked_number = card_number[:7] + ' ' + card_number[8:12] + ' ******** ' + card_number[20:24]
    return masked_number


def mask_account_number(account_number):
    masked_number = account_number[:4] + ' ' + "**" + account_number[21:25]
    return masked_number
