import json
import pathlib
from schematicspy.parser.json import JsonParser


current_folder = pathlib.Path(__file__).parent.resolve()
collection = current_folder / "mocks" / "collection.json"
json_file = open(collection).read()


def test_json_parser_init():
    json_parser = JsonParser(json_file)

    assert isinstance(json_parser, object) == True


def test_json_parser_dump():
    json_parser = JsonParser(json_file)
    dump = json_parser.dump()
    direct_dump = json.dumps(json.loads(json_file))

    assert direct_dump == dump
