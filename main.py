from pathlib import Path

from cli import configure_argument_parser
from exception import FileNameArgumentMissing, ReportTypeMissing
from outputs import get_pretty_table
from parser.parser_log import ParserLog
from reports.average import AverageReport


CHOICE_CLASS_REPORT = {
    'average': AverageReport,
}


def validate_args(args):
    if args.file is None:
        raise FileNameArgumentMissing(
            'Отсутствует обязательный аргумент запуска: -f, --file'
        )
    if args.report is None:
        raise ReportTypeMissing(
            'Отсутствует обязательный аргумент запуска: -r, --report '
            f'Доступные отчёты: {", ".join(CHOICE_CLASS_REPORT.keys())}'
        )


def process_log_file(name_file: str, args):
    file_path = Path.cwd()/'logs'/name_file
    parser_log = ParserLog(file_path)

    if args.date:
        dict_obj = parser_log.parse_log(args.date)
    else:
        dict_obj = parser_log.parse_log()

    report = CHOICE_CLASS_REPORT[args.report](dict_obj)
    results = report.get_report()
    get_pretty_table(results)


def main(args):
    validate_args(args)
    for name_file in args.file:
        process_log_file(name_file, args)


if __name__ == '__main__':
    arg_parser = configure_argument_parser()
    args = arg_parser.parse_args()
    main(args)
