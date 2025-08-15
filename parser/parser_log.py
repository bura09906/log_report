import json
from collections import defaultdict
from pathlib import Path

from exception import EmptyFileError
from settings import DATE_INDEX_IN_ISO, ISO_DATETIME_SEPARATOR, KEY_TIMESTAMP

from .models_log import LogEntry


class ParserLog:

    def __init__(self, file_path: Path):
        self.file_path: Path = file_path
        self.dict_obj: dict[str, list[LogEntry]] = defaultdict(list)

    def file_read(self) -> list:
        with open(self.file_path) as file:
            list_raw = file.readlines()

            if not list_raw:
                raise EmptyFileError(
                    f'Файл {self.file_path.name} пустой'
                )

            return list_raw

    def parse_log(self, date: str = None) -> dict[str, list[LogEntry]]:
        list_raw = self.file_read()
        for raw in list_raw:
            raw = json.loads(raw)

            if (
                date and raw[KEY_TIMESTAMP].split(ISO_DATETIME_SEPARATOR)
                [DATE_INDEX_IN_ISO] != date
            ):
                continue

            obj = LogEntry.from_dict(raw)
            self.dict_obj[raw['url']].append(obj)
        return self.dict_obj
