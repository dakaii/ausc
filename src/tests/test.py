import unittest

from temp_analyzer import TemperatureAnalyzer

_MOCK_INPUT_PATH = 'tests/mock_files/mock_data.json'


class TestTemperatureAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = TemperatureAnalyzer()

    def tearDown(self):
        del self.analyzer

    def test_analyze_returns_correct_values(self):
        output = self.analyzer.analyze(_MOCK_INPUT_PATH)
        correct_values = [
            {'average': 3.77, 'id': 'a', 'median': 3.65, 'mode': [3.53]},
            {'average': 4.08, 'id': 'b', 'median': 4.14, 'mode': [4.15]},
            {'average': 3.72, 'id': 'c', 'median': 3.95, 'mode': [3.96, 3.36]}]
        self.assertEqual(output, correct_values)


if __name__ == '__main__':
    unittest.main()
