import logging

logger = logging.getLogger(__name__)

def read_file(input_filepath):
    with open(input_filepath, encoding="utf-8") as file:
        read_data = file.read()
    logger.info("Read file %s", input_filepath)
    return read_data

def write_file(output_filepath, content):
    with open(output_filepath, 'w', encoding="utf-8") as file:
        file.write(content)
    logger.info("Wrote content into output_file %s", output_filepath)

