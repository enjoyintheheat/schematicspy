import json


class JsonParser:
    def __init__(self, text: str):
        self._raw_json = json.loads(text)

    def dump(self) -> str:
        return json.dumps(self._raw_json)

    def __repr__(self):
        str_len = len(self._raw_json.encode("utf-8"))
        return f"<JsonParser [{str_len} Bytes]>"
