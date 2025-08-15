import pytest

from cli import configure_argument_parser
from exception import FileNameArgumentMissing, ReportTypeMissing
from main import validate_args, main


class TestMain:

    @pytest.mark.parametrize(
        "args_list, expected_exception",
        [
            (["-r", "average"], FileNameArgumentMissing),
            (["-f", "log.txt"], ReportTypeMissing),
            (["-f", "log.txt", "-r", "average"], None),
        ]
    )
    def test_cli_args(self, args_list, expected_exception):
        parser = configure_argument_parser()
        args = parser.parse_args(args_list)

        if expected_exception:
            with pytest.raises(expected_exception):
                validate_args(args)
        else:
            validate_args(args)

    def test_run_main(self, json_file, capsys, monkeypatch):
        monkeypatch.setattr(
            "pathlib.Path.cwd", lambda: json_file.parent.parent
        )

        args_cli = ["-f", json_file.name, "-r", "average"]
        parser = configure_argument_parser()
        args = parser.parse_args(args_cli)

        main(args)

        captured = capsys.readouterr()
        output = captured.out

        assert "handler" in output
        assert "total" in output
        assert "avg_response_time" in output
