# 以下のテストケースを考慮します
#
# 1. get_logger関数が正しくロガーを返すか。
# 2. 返されたロガーが正しいレベルで設定されているか。
# 3. 返されたロガーがコンソールにログを出力する設定になっているか。
# 4. output_to_fileがTrueの場合、返されたロガーがファイルにログを出力する設定になっているか。


import logging
from pathlib import Path

from snippets_python.logging.logger import (
    get_logger,
    TextFormatter,
    JSONFormatter,
)


def test_get_logger():
    logger_name = "test_text_logger"
    logger = get_logger(logger_name)

    # ロガーが正しく返されているか
    assert isinstance(logger, logging.Logger)
    assert logger.name == logger_name

    # ロガーのレベルが正しいか
    assert logger.level == logging.DEBUG

    # コンソールへの出力設定が正しいか
    ch = logger.handlers[0]
    assert isinstance(ch, logging.StreamHandler)
    assert isinstance(ch.formatter, TextFormatter)


def test_get_json_logger():
    logger_name = "test_json_logger"
    logger = get_logger(logger_name, formatter=JSONFormatter)

    # ロガーが正しく返されているか
    assert isinstance(logger, logging.Logger)
    assert logger.name == logger_name

    # ロガーのレベルが正しいか
    assert logger.level == logging.DEBUG

    # コンソールへの出力設定が正しいか
    ch = logger.handlers[0]
    assert isinstance(ch, logging.StreamHandler)
    assert isinstance(ch.formatter, JSONFormatter)


def test_get_logger_output_to_file():
    logger_name = "test_logger_file"
    logger = get_logger(logger_name, output_to_file=True)

    # ファイルへの出力設定が正しいか
    fh = logger.handlers[1]
    assert isinstance(fh, logging.FileHandler)
    assert isinstance(fh.formatter, TextFormatter)
    assert fh.baseFilename.endswith("app.log")


def teardown_function():
    # テスト終了後にapp.logを削除
    log_file = Path("app.log")
    if log_file.exists():
        log_file.unlink()
