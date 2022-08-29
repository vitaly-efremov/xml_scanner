import time
from pathlib import Path

from data_generator import generate_data

if __name__ == '__main__':
    data_path = 'data'
    Path(data_path).mkdir(parents=True, exist_ok=True)
    started_at = time.perf_counter()
    generate_data(path=data_path)
    print(f'Data is successfully generated in {time.perf_counter() - started_at:.2f} sec.')
