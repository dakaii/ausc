import argparse
import json

from settings import INPUT_PATH, OUTPUT_PATH


def get_constants():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-i", "--input_path", help="Input File Path")
    paths = argparser.parse_args()
    input_path = paths.input_path if paths.input_path else INPUT_PATH
    output_path = OUTPUT_PATH
    return input_path, output_path


def rounding(val):
    return round(val, 2)


def writefile(fname, data):
    '''
     When the file is not found, this function create a new file
     and writes to it.
    '''
    with open(fname, 'w') as f:
        json.dump(data, f, ensure_ascii=False)


class Parser:
    def __call__(self, fpath):
        try:
            with open(fpath) as f:
                json_input = json.load(f)
            return self._aggregate_input(json_input)
        except IOError as err:
            sys.exit("The required file {0} was not found.".format(fpath))

    def _aggregate_input(self, json_input):
        temps = {}
        for data in json_input:
            if data['id'] in temps:
                temps[data['id']].append(data['temperature'])
            else:
                temps[data['id']] = [data['temperature']]
        return temps
