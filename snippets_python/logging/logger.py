import json
import logging


class TextFormatter(logging.Formatter):
    def __init__(
        self,
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt=None,
    ):
        super().__init__(fmt, datefmt)


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "name": record.name,
            "levelname": record.levelname,
            "message": record.getMessage(),
            "pathname": record.pathname,
            "lineno": record.lineno,
            "funcName": record.funcName,
        }
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_record, ensure_ascii=False)


def get_logger(
    name: str,
    formatter: logging.Formatter = TextFormatter,
    level=logging.DEBUG,
    output_to_file: bool = False,
) -> logging.Logger:
    # ロガーの設定
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # フォーマットの設定
    formatter = formatter()

    # コンソールへの出力設定
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if output_to_file:
        # ファイルへの出力設定
        fh = logging.FileHandler("app.log")
        fh.setLevel(level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
