from dataclasses import dataclass

from settings import FIELD_TIMESTAMP, KEY_TIMESTAMP


@dataclass
class LogEntry:
    timestamp: str
    status: int
    url: str
    request_method: str
    response_time: float
    http_user_agent: str

    @classmethod
    def from_dict(cls, data: dict):
        cls.validate(data)
        timestamp = data.pop(KEY_TIMESTAMP)
        data[FIELD_TIMESTAMP] = timestamp
        return cls(**data)

    @classmethod
    def validate(cls, data: dict):
        allowed_keys = set(cls.__annotations__.keys()) | {KEY_TIMESTAMP}
        for key in data.keys():
            if key not in allowed_keys:
                raise ValueError(f"Недопустимый ключ: '{key}'")
        expected_types = {
            "@timestamp": str,
            "status": int,
            "url": str,
            "request_method": str,
            "response_time": float,
            "http_user_agent": str,
        }
        for key, value in data.items():
            expected_type = expected_types.get(key)
            if expected_type and not isinstance(value, expected_type):
                raise ValueError(
                    f"Неверный формат данных: ключ '{key}' "
                    f"(ожидался {expected_type.__name__}, "
                    f"получен {type(value).__name__})"
                )
