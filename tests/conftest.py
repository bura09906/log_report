from parser.models_log import LogEntry
from parser.parser_log import ParserLog

import pytest

from reports.average import AverageReport


@pytest.fixture
def dir_log(tmp_path):
    dir_path = tmp_path/'logs'
    dir_path.mkdir()
    return dir_path


@pytest.fixture
def empty_file(dir_log):
    file_path = dir_log/'empty_file.log'
    file_path.touch()
    return file_path


@pytest.fixture
def json_lines():
    correct_line = (
        '{"@timestamp": "2025-06-23T13:59:56+00:00", "status": 200, "url": '
        '"/api/homeworks/...", "request_method": "GET", "response_time": '
        '0.112, "http_user_agent": "..."}'
    )
    correct_line1 = (
        '{"@timestamp": "2025-06-23T13:59:57+00:00", "status": 200, "url": '
        '"/api/context/...", "request_method": "GET", "response_time": '
        '0.144, "http_user_agent": "..."}'
    )
    correct_line2 = (
        '{"@timestamp": "2025-06-22T13:59:57+00:00", "status": 200, "url": '
        '"/api/users/...", "request_method": "GET", "response_time": '
        '0.14, "http_user_agent": "..."}'
    )
    correct_line3 = (
        '{"@timestamp": "2025-06-22T14:59:57+00:00", "status": 200, "url": '
        '"/api/users/...", "request_method": "GET", "response_time": '
        '0.28, "http_user_agent": "..."}'
    )
    return [correct_line, correct_line1, correct_line2, correct_line3]


@pytest.fixture
def json_line(dir_log):
    line = (
        '{"@timestamp": "2025-06-22T13:59:56+00:00", "status": 200, "url": '
        '"/api/homeworks/...", "request_method": "GET", "response_time": '
        '0.112, "http_user_agent": "..."}'
    )

    file_path = dir_log / "test_logs_1.json"
    file_path.touch()
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    return file_path


@pytest.fixture
def incorrect_json_lines():
    correct_line1 = (
        '{"@timestamp": "2025-06-22T13:59:56+00:00", "status": 200, "url": '
        '"/api/homeworks/...", "request_method": "GET", "response_time": '
        '0.112, "http_user_agent": "..."}'
    )
    correct_line2 = (
        '{"@timestamp": "2025-06-22T13:59:57+00:00", "status": 200, "url": '
        '"/api/homeworks/...", "request_method": "GET", "response_time": '
        '0.144, "http_user_agent": "..."}'
    )
    incorrect_line = (
        '"@timestamp": "2025-06-22T13:59:57+00:00", "status": 200, "url": '
        '"/api/homeworks/...", "request_method": "GET", "response_time": '
        '0.14, "http_user_agent": "..."'
    )
    return [correct_line1, correct_line2, incorrect_line]


@pytest.fixture
def expected_logentry():
    expectd_logentry = LogEntry(
        timestamp="2025-06-22T13:59:56+00:00",
        status=200,
        url="/api/homeworks/...",
        request_method="GET",
        response_time=0.112,
        http_user_agent="...",
    )
    return expectd_logentry


@pytest.fixture
def incorrect_json_file(dir_log, incorrect_json_lines):
    file_path = dir_log / "test_logs.json"
    file_path.touch()
    with open(file_path, "w", encoding="utf-8") as f:
        for line in incorrect_json_lines:
            f.write(line + "\n")
    return file_path


@pytest.fixture
def json_file(dir_log, json_lines):
    file_path = dir_log / "test_logs.json"
    file_path.touch()
    with open(file_path, "w", encoding="utf-8") as f:
        for line in json_lines:
            f.write(line + "\n")
    return file_path


@pytest.fixture
def json_file_2(dir_log, json_lines):
    file_path = dir_log / "test_logs_2.json"
    file_path.touch()
    with open(file_path, "w", encoding="utf-8") as f:
        for line in json_lines:
            f.write(line + "\n")
    return file_path


@pytest.fixture
def dict_obj_one_logentry(json_line):
    parser = ParserLog(json_line)
    dict_obj = parser.parse_log()
    return dict_obj


@pytest.fixture
def dict_obj_logentry(json_file):
    parser = ParserLog(json_file)
    dict_obj = parser.parse_log()
    return dict_obj


@pytest.fixture
def expected_report():
    return [
        ("/api/homeworks/...", 1, 0.112),
        ("/api/context/...", 1, 0.144),
        ("/api/users/...", 2, 0.21),
    ]


@pytest.fixture
def get_report(dict_obj_logentry):
    report = AverageReport(dict_obj_logentry)
    results = report.get_report()
    return results


@pytest.fixture
def invalid_data_type(dir_log):
    file_path = dir_log / 'invalid_data_type.log'
    file_path.touch()
    invalid_type_status = (
        '{"@timestamp": "2025-06-22T13:59:57+00:00", "status": "200", "url": '
        '"/api/homeworks/...", "request_method": "GET", "response_time": '
        '0.144, "http_user_agent": "..."}'
    )
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(invalid_type_status)

    return file_path


@pytest.fixture
def unexpected_key(dir_log):
    file_path = dir_log / 'invalid_data_type.log'
    file_path.touch()
    unexpected_kye_ip_address = (
        '{"@timestamp": "2025-06-22T13:59:57+00:00", "status": "200", "url": '
        '"/api/homeworks/...", "request_method": "GET", "response_time": '
        '0.144, "http_user_agent": "...", "ip_address": 0.0.0.0.0}'
    )
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(unexpected_kye_ip_address)

    return file_path
