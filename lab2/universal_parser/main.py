import argparse
import configparser
from universal_parser.serializer_factory import SerializerFactory
from universal_parser.logger.logger import get_logger
logger = get_logger(__name__)

def main():
    def parse(old_format, new_format, file_name):
        factory = SerializerFactory()
        old_format_parser = factory.get_serializer(old_format)
        new_format_parser = factory.get_serializer(new_format)
        intermediate_data = old_format_parser.load(file_name)
        new_format_parser.dump(intermediate_data, file_name.rsplit('.', 1)[0]+'.'+new_format.lower())
        logger.info(f"{file_name} was successfully converted into {file_name.rsplit('.', 1)[0]+'.'+new_format.lower()}")

    try:
        parser = argparse.ArgumentParser(description='JSON/TOML/YAML/PICKLE Serializer')
        parser.add_argument('-config', '--config_file', type=str, help='configuration file with settings, primary used')
        parser.add_argument('-old', '--old_format', type=str, help="old format, format of your current file")
        parser.add_argument('-new', '--new_format', type=str, help="new format, format of your future file")
        parser.add_argument('-file', '--file_path', type=str, help="path to your file")
        args = parser.parse_args()
        if args.config_file is not None:
            config = configparser.ConfigParser()
            config.read(args.config_file)
            old_format = config['Serializer']['old_format']
            new_format = config['Serializer']['new_format']
            file_path = config['Serializer']['file_path']
        else:
            old_format = args.old_format
            new_format = args.new_format
            file_path = args.file_path
        if None in (old_format, new_format, file_path):
            raise ValueError('Some arguments left unfilled')
        parse(old_format, new_format, file_path)
    except Exception as error:
        logger.error(error, exc_info=True)