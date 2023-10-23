import logging

from snippets_python.logging.logger import get_logger


def main():
    logger = get_logger(__name__, level=logging.INFO)

    logger.debug("Debug message")
    logger.info("Information message")
    logger.warning("Warning message")
    logger.error("Error message")

    try:
        x = 1 / 0
        logger.info(x)
    except Exception:
        logger.exception("An exception occurred.")


if __name__ == "__main__":
    main()
