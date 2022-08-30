import asyncio
import timeit
from pathlib import Path

from service.csv_writer.async_csv_writer import AsyncCSVWriter
from service.xml_service import extract_xml_data


class ReportGenerator:
    def __init__(
        self,
        variables_report_filename='report/variables_report.csv',
        objects_report_filename='report/objects_report.csv',
    ):
        self._variables_csv = AsyncCSVWriter(variables_report_filename)
        self._objects_csv = AsyncCSVWriter(objects_report_filename)

    async def generate(self, data_path: Path):
        await asyncio.gather(
            self._variables_csv.write_header(columns=['id', 'level']),
            self._objects_csv.write_header(columns=['id', 'object_name']),
        )

        zip_files = (file for file in data_path.iterdir() if file.is_file())
        for zip_file in zip_files:
            await self._proceed_zip_file(zip_file)

    async def _proceed_zip_file(self, zip_file):
        variable_rows = []
        object_rows = []
        for xml_data in extract_xml_data(zip_file):
            variable_rows.append([xml_data.xml_id, xml_data.level])
            object_rows += [[xml_data.xml_id, name] for name in xml_data.object_names]

        await asyncio.gather(
            self._variables_csv.write_rows(variable_rows),
            self._objects_csv.write_rows(object_rows),
        )


def main():
    report_generator = ReportGenerator()
    path = Path('../data')
    asyncio.run(report_generator.generate(path))


if __name__ == '__main__':
    print(timeit.timeit(main, number=100))
