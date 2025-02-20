
def get_mask_card_number(card_number: str) -> str:
    if not card_number.isdigit() or len(card_number) != 16:
        return "Ошибка формата"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def get_mask_account(account_number: str) -> str:
    if not account_number.isdigit() or len(account_number) < 20:
        return "Ошибка формата"
    return f"**{account_number[-6:]}"

# Функция определения типа счета
def mask_account_card(data: str) -> str:
    if data.startswith("Счет"):
        return get_mask_account(data.split()[1])
    else:
        return get_mask_card_number(data.split()[1])

# Функция обработки даты
def get_date(operation_date: str) -> str:
    try:
        from datetime import datetime
        date_obj = datetime.strptime(operation_date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Неверный формат даты"

# Фильтрация операций
def filter_by_state(operations: list, state: str) -> list:
    return [op for op in operations if op.get("state") == state]

# Сортировка операций
def sort_by_date(operations: list, reverse: bool = True) -> list:
    return sorted(operations, key=lambda x: x.get("date", ""), reverse=reverse)