import asyncio
import time
from pathlib import Path

from data_generator import generate_data
from service.async_report import ReportGenerator

if __name__ == '__main__':
    data_path = Path('data')
    data_path.mkdir(parents=True, exist_ok=True)

    generation_started_at = time.perf_counter()
    generate_data(path=data_path)
    print(f'Data is generated in {time.perf_counter() - generation_started_at:.2f} sec.')

    report_generation_started_at = time.perf_counter()
    report_generator = ReportGenerator()
    asyncio.run(report_generator.generate(data_path))
    print(f'Report is generated in {time.perf_counter() - report_generation_started_at:.2f} sec.')
