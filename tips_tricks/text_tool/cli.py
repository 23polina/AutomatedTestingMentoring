import argparse
import logging
import sys
from logging import basicConfig

from text_tool.file_io import read_file, write_file
from text_tool.processor import get_word_frequency_report


logger = logging.getLogger(__name__)

def setup_logging():
    file_handler = logging.FileHandler("logs.log", encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.ERROR)

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                        handlers=[file_handler, stream_handler]
    )


def process_file(input_path, output_path):
    text = read_file(input_path)
    content = get_word_frequency_report(text)
    write_file(output_path, content)
    logger.info("Processed %s and saved to %s", input_path, output_path)


def main():
    setup_logging()
    parser = argparse.ArgumentParser(prog="TextToolParser",
                                     description="The program reads a text file, processes its content, "
                                                 "and outputs the result to another file ")
    parser.add_argument('input_file_path')
    parser.add_argument('output_file_path')
    args = parser.parse_args()
    try:
        process_file(args.input_file_path, args.output_file_path)
    except FileNotFoundError as e:
        logger.error("File not found %s" ,e.filename)
        sys.exit(1)
    except PermissionError as e:
        logger.error("No permissions to a file %s", e.filename)
        sys.exit(1)
    except OSError as e:
        logger.error("File error %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()

