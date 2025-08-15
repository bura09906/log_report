from abc import ABC, abstractmethod

from parser.models_log import LogEntry


class BaseReport(ABC):

    def __init__(self, log: dict[str, list[LogEntry]]):
        self.log = log
        self.results = []

    @abstractmethod
    def get_report(self) -> list[tuple]:
        pass
