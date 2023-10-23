# test_main_module.py

import pytest
from snippets_python.exception.main import process_data, CustomError


def test_process_data_with_data():
    """データが存在する場合のテスト"""
    data = "sample data"
    # 例外が発生しないことを確認
    assert process_data(data) is None


def test_process_data_without_data():
    """データが存在しない場合のテスト"""
    data = None
    # CustomErrorが発生することを確認
    with pytest.raises(CustomError, match="Data is missing"):
        process_data(data)
