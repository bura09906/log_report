import json
from parser.models_log import LogEntry
from parser.parser_log import ParserLog

import pytest

from exception import EmptyFileError


class TestParseLog:

    def test_empty_file(self, empty_file):
        with pytest.raises(EmptyFileError):
            parser = ParserLog(empty_file)
            parser.file_read()

    def test_not_found_file(self, dir_log, empty_file):
        fake_file = dir_log/'file_not_found.log'
        with pytest.raises(FileNotFoundError):
            parser = ParserLog(fake_file)
            parser.file_read()

    def test_incorrect_file(self, incorrect_json_file):
        with pytest.raises(json.JSONDecodeError):
            parser = ParserLog(incorrect_json_file)
            parser.parse_log()

    def test_invalid_data_type(self, invalid_data_type):
        with pytest.raises(ValueError):
            parser = ParserLog(invalid_data_type)
            parser.parse_log()

    def test_unexpected_key(self, unexpected_key):
        with pytest.raises(ValueError):
            parser = ParserLog(unexpected_key)
            parser.parse_log()

    def test_parser_returns_correct_types(self, dict_obj_logentry):
        assert isinstance(dict_obj_logentry, dict)

        for key, value in dict_obj_logentry.items():
            assert isinstance(key, str)
            for obj in value:
                assert isinstance(obj, LogEntry)

    def test_parse_log(self, dict_obj_one_logentry, expected_logentry):
        obj = dict_obj_one_logentry['/api/homeworks/...'][0]
        assert obj == expected_logentry
