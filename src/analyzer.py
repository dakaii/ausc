import json
import sys
from pprint import pprint

from util import rounding, writefile, Parser


class Analyzer(object):

    def __init__(self, input_path, output_path):
        self.parser = Parser()
        self.output = []
        self.input_path = input_path
        self.output_path = output_path

    def __call__(self):
        self.analyze()
        writefile(self.output_path, self.output)
        self.console_print()

    def analyze(self):
        raise NotImplementedError

    def console_print(self):
        pprint(self.output)


class TemperatureAnalyzer(Analyzer):

    def analyze(self):
        inputted_data = self.parser(self.input_path)
        for key, lis in inputted_data.items():
            self.output.append({
                'id': key,
                'average': self._average(lis),
                'median': self._median(lis),
                'mode': self._mode(lis),
            })
        return self.output

    def _average(self, lis):
        return rounding(sum(lis) / float(len(lis)))

    def _median(self, lis):
        temps = sorted(lis)
        mid_idx = int(len(temps) / 2)
        if len(temps) % 2 == 1:
            return rounding(temps[mid_idx])
        else:
            return rounding((temps[mid_idx] + temps[mid_idx - 1]) / 2.0)

    def _mode(self, lis):
        count = {rounding(val): lis.count(val) for val in lis}
        max_freq = max(count.values())
        return [val for val, freq in count.items() if freq == max_freq]
