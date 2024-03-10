from src.utils import sorted_file
from src.utils import format_date
from src.utils import mask_card_number
from src.utils import mask_account_number


def main():
    five_dicts = sorted_file()
    for operation in five_dicts:
        description = operation['description']
        from_account = operation.get('from', 'None')
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        print(format_date(operation['date']), description)
        if from_account != 'None':
            print(mask_card_number(operation['from']), '->', mask_account_number(operation['to']))
        else:
            print(mask_account_number(operation['to']))
        print(f"{amount} {currency}\n")


main()
