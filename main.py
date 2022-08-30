import time
from pathlib import Path

from data_generator import generate_data
from service.report_service.multiprocessing_report import ReportGenerator

if __name__ == '__main__':
    data_path = Path('data')
    data_path.mkdir(parents=True, exist_ok=True)

    generation_started_at = time.perf_counter()
    generate_data(path=data_path)
    print(f'Data is generated in {time.perf_counter() - generation_started_at:.2f} sec.')

    report_path = Path('report')
    report_path.mkdir(parents=True, exist_ok=True)
    report_generation_started_at = time.perf_counter()
    report_generator = ReportGenerator(
        variables_report_filename=report_path.joinpath('variables_report.csv'),
        objects_report_filename=report_path.joinpath('objects_report.csv'),
    )
    report_generator.generate(data_path)
    print(f'Report is generated in {time.perf_counter() - report_generation_started_at:.2f} sec.')
