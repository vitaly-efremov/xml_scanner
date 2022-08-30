import asyncio
import timeit
from pathlib import Path
from typing import Iterator

from service.csv_writer.async_csv_writer import AsyncCSVWriter
from service.xml_service import XMLData
from service.xml_service import extract_xml_data
from utils import grouper


class ReportGenerator:
    def __init__(
        self,
        variables_report_filename='variables_report.csv',
        objects_report_filename='objects_report.csv',
    ):
        self._variables_csv = AsyncCSVWriter(variables_report_filename)
        self._objects_csv = AsyncCSVWriter(objects_report_filename)

    async def generate(self, data_path: Path, batch_size=500):
        await asyncio.gather(
            self._variables_csv.write_header(columns=['id', 'level']),
            self._objects_csv.write_header(columns=['id', 'object_name']),
        )

        zip_files = (file for file in data_path.iterdir() if file.is_file())
        xml_collection = (xml_data for zip_file in zip_files for xml_data in extract_xml_data(zip_file))
        for batch in grouper(xml_collection, n=batch_size):
            await self._proceed_xml_collection(xml_collection=batch)

    async def _proceed_xml_collection(self, xml_collection: Iterator[XMLData]):
        variable_rows = []
        object_rows = []
        for xml_data in xml_collection:
            variable_rows.append([xml_data.xml_id, xml_data.level])
            object_rows += [[xml_data.xml_id, name] for name in xml_data.object_names]

        await asyncio.gather(
            self._variables_csv.write_rows(variable_rows),
            self._objects_csv.write_rows(object_rows),
        )


if __name__ == '__main__':
    path = Path('../data')
    report_generator = ReportGenerator()
    print(timeit.timeit(lambda: asyncio.run(report_generator.generate(path)), number=100))
