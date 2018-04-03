import json
import argparse


def load_data(filepath):
    with open(filepath, 'r') as json_file:
        parsed_json = json.load(json_file)
    return parsed_json


def pretty_print_json(json_data, indent=4, ensure_ascii=False):
    print(
        json.dumps(
            json_data,
            indent=indent,
            ensure_ascii=ensure_ascii
        )
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Tool to prettify output of json files'
    )

    parser.add_argument(
        '-f', '--filepath',
        help='path to json file',
        required=True
    )

    args = parser.parse_args()

    parsed_json_file = load_data(args.filepath)

    pretty_print_json(parsed_json_file)

