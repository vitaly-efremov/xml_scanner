import csv
from typing import Iterable
from typing import List


class CSVWriter:
    def __init__(self, filename):
        self._filename = filename

    def write_rows(self, rows: Iterable[List[str]]):
        self._write_rows(rows, file_open_mode='a')

    def write_header(self, columns: List[str]):
        self._write_rows(rows=[columns], file_open_mode='w')

    def _write_rows(self, rows: Iterable[List[str]], file_open_mode: str):
        with open(self._filename, file_open_mode) as file:
            writer = csv.writer(file)
            writer.writerows(rows)
