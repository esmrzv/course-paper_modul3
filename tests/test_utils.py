from src.utils import sorted_file, filtered_file, json_file_path, format_date, load_file
import pytest
import operator


@pytest.fixture
def data_path():
    return json_file_path


def test_load_file(data_path):
    assert type(load_file(data_path)) == list


def test_filtered_file(data_path):
    filtered_data = filtered_file()
    for item in filtered_data:
        assert item.get('date') is not None


def test_sorted_file(data_path):
    filtered_data = filtered_file()
    data_sorted = sorted(filtered_data, key=operator.itemgetter('date'), reverse=True)
    list_executed_operation = sorted_file()

    count = 0
    for operation in data_sorted:
        if operation['state'] == "EXECUTED":
            count += 1
            assert operation in list_executed_operation
            if count == 5:
                break


def test_format_date_valid():
    date_str = "2022-12-31T23:59:59"
    expected_result = "31.12.2022"
    assert format_date(date_str) == expected_result


def test_mask_card_number():
    pass
