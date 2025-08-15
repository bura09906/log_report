

class TestReport:

    def test_get_report(self, get_report, expected_report):
        assert get_report == expected_report
