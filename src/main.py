from analyzer import TemperatureAnalyzer
from util import get_constants


def main():
    input_path, output_path = get_constants()
    temp_analyzer = TemperatureAnalyzer(input_path, output_path)
    temp_analyzer()


if __name__ == '__main__':
    main()
