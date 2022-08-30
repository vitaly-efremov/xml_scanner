from typing import Iterable
from typing import List

import aiofiles


class AsyncCSVWriter:
    def __init__(self, filename, separator=','):
        self._filename = filename
        self._separator = separator

    async def write_header(self, columns: List[str]):
        await self._write_rows(rows=[columns], file_open_mode='w')

    async def write_rows(self, rows: Iterable[List[str]]):
        await self._write_rows(rows, file_open_mode='a')

    async def _write_rows(self, rows: Iterable[List[str]], file_open_mode: str):
        formatted_rows = (self._separator.join(f'"{value}"' for value in values) for values in rows)
        content = '\n'.join(formatted_rows)
        async with aiofiles.open(self._filename, file_open_mode) as file:
            await file.write(content + '\n')
