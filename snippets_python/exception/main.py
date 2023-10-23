from typing import Optional

from snippets_python.logging.logger import get_logger

logger = get_logger(__name__)


class CustomError(Exception):
    """Application-specific custom exception"""


def process_data(data: Optional[int]):
    if data is None:
        raise CustomError("Data is missing")


def main():
    data = None  # In this example, data is None

    try:
        process_data(data)
    except CustomError as e:
        logger.error(f"Custom error occurred: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    finally:
        logger.info("Data processing finished")


if __name__ == "__main__":
    main()
