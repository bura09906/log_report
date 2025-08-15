import argparse


def configure_argument_parser():
    parser = argparse.ArgumentParser(description='Парсер файлов логов проекта')
    parser.add_argument(
        '-f',
        '--file',
        help='Путь к файлу с логами',
        nargs='+',
    )
    parser.add_argument('-r', '--report', help='Назвние отчета',)
    parser.add_argument(
        '-d',
        '--date',
        help='Получить отчет за указанную дату. Формат: YYYY:MM:DD',
    )
    return parser
