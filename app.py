import argparse
from tinydb import TinyDB
from utils import detect_type
import os
import json


def load_templates():
    db_path = os.path.join(os.path.dirname(__file__), "db.json")
    db = TinyDB(db_path)
    return db.all()


def parse_args():
    parser = argparse.ArgumentParser(description="Поиск подходящего шаблона формы")
    parser.add_argument("command", choices=["get_tpl"], help="Команда для запуска")
    known_args, unknown_args = parser.parse_known_args()

    data = {}
    for arg in unknown_args:
        if arg.startswith("--") and "=" in arg:
            key, val = arg[2:].split("=", 1)
            data[key] = val

    return known_args.command, data


def match_template(query, templates):
    for tpl in templates:
        tpl_fields = {k: v for k, v in tpl.items() if k != "name"}
        matched = True
        for field, ftype in tpl_fields.items():
            if field not in query or detect_type(query[field]) != ftype:
                matched = False
                break
        if matched:
            return tpl["name"]
    return None


def build_response(query):
    return {k: detect_type(v) for k, v in query.items()}


def main():
    command, query = parse_args()
    templates = load_templates()

    if command == "get_tpl":
        if not query:
            print("⚠️ Не переданы параметры запроса. Пример: --login=user@example.com --birth=2024-01-01")
            return

        matched = match_template(query, templates)
        if matched:
            print(matched)
        else:
            print(json.dumps(build_response(query), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
