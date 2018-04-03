import json
import argparse


def load_data(filepath):
    with open(filepath, 'r') as json_file:
        parsed_json = json.load(json_file)
    return parsed_json


def pretty_print_json(json_obj, indent=4, ensure_ascii=False):
    print(
        json.dumps(
            json_obj,
            indent=indent,
            ensure_ascii=ensure_ascii
        )
    )


def get_args():
    parser = argparse.ArgumentParser(
        description='Tool to prettify output of json files'
    )

    parser.add_argument(
        '-f', '--filepath',
        help='path to json file',
        required=True
    )
    return parser.parse_args()


if __name__ == '__main__':

    args = get_args()

    parsed_json = load_data(args.filepath)

    pretty_print_json(parsed_json)

