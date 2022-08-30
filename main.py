import time
from pathlib import Path

from data_generator import generate_data
from service.report_service.multiprocessing_report import ReportGenerator


def generate_test_data(data_path: Path):
    """ Generates test data in **data_path* dir """
    generation_started_at = time.perf_counter()
    generate_data(path=data_path)
    print(f'Data is generated in {time.perf_counter() - generation_started_at:.2f} sec.')


def generate_report(data_path: Path, report_path: Path):
    """
        Generates report (**objects_report.csv** and **variables_report.csv** files) in **report_path** dir
        using files from **data_path**
    """
    report_generation_started_at = time.perf_counter()
    report_generator = ReportGenerator(
        variables_report_filename=report_path.joinpath('variables_report.csv'),
        objects_report_filename=report_path.joinpath('objects_report.csv'),
    )
    report_generator.generate(data_path)
    print(f'Report is generated in {time.perf_counter() - report_generation_started_at:.2f} sec.')


def run(new_test_data=True):
    data_path = Path('data')
    data_path.mkdir(parents=True, exist_ok=True)
    if new_test_data:
        generate_test_data(data_path)

    report_path = Path('report')
    report_path.mkdir(parents=True, exist_ok=True)
    generate_report(data_path=data_path, report_path=report_path)


if __name__ == '__main__':
    run()
