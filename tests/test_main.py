import pytest
from main import *

@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("123456", "Ошибка формата"),
    ("", "Ошибка формата"),
    ("invalid", "Ошибка формата")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("account_number, expected", [
    ("12345678901234567890", "**34567890"),
    ("12345", "Ошибка формата"),
    ("notanumber", "Ошибка формата")
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

@pytest.mark.parametrize("data, expected", [
    ("Счет 12345678901234567890", "**34567890"),
    ("Visa 1234567890123456", "1234 56** **** 3456"),
    ("", "Ошибка формата")
])
def test_mask_account_card(data, expected):
    assert mask_account_card(data) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2023-01-01T00:00:00.000000", "01.01.2023"),
    ("invalid", "Неверный формат даты")
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected

@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00.000000"},
        {"id": 2, "state": "PENDING", "date": "2023-01-02T00:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03T00:00:00.000000"}
    ]

def test_filter_by_state(sample_operations):
    executed = filter_by_state(sample_operations, "EXECUTED")
    assert len(executed) == 2
    assert all(op["state"] == "EXECUTED" for op in executed)

def test_sort_by_date(sample_operations):
    sorted_ops = sort_by_date(sample_operations)
    dates = [op["date"] for op in sorted_ops]
    assert dates == ["2023-01-03T00:00:00.000000", "2023-01-02T00:00:00.000000", "2023-01-01T00:00:00.000000"]