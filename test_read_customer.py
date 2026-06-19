from read_customer import parse_record
import pytest

def test_parse_record():
    line = "100001JOHN SMITH          SAV025000.50"
    customer = parse_record(line)
    assert customer["customer_id"] == "100001"
    assert customer["customer_name"] == "JOHN SMITH"
    assert customer["account_type"] == "SAV"
    assert customer["balance"] == 25000.50

def test_parse_record_second_customer():
    line = "100002MARY JONES          CUR015000.75"
    customer = parse_record(line)
    assert customer["customer_id"] == "100002"
    assert customer["customer_name"] == "MARY JONES"
    assert customer["account_type"] == "CUR"
    assert customer["balance"] == 15000.75

def test_invalid_balance():
    line = "100001JOHN SMITH          SAVABCDEF"
    with pytest.raises(ValueError):
        parse_record(line)