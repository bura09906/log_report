from reports.base import BaseReport
from settings import ROUND_PRECISION


class AverageReport(BaseReport):

    def get_report(self) -> list[tuple]:
        for handler, data in self.log.items():
            total = len(data)
            response_time: int = 0

            for obj in data:
                response_time += obj.response_time

            avg_response_time = round(response_time/total, ROUND_PRECISION)
            result = handler, total, avg_response_time
            self.results.append(result)

        return self.results
