import timeit
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from pathlib import Path

from service.csv_writer import СSVWriter
from service.xml_service import extract_xml_data


def proceed_zip_file(zip_file, variables_report_filename, objects_report_filename):
    variables_csv = СSVWriter(variables_report_filename)
    objects_csv = СSVWriter(objects_report_filename)

    variable_rows = []
    object_rows = []
    for xml_data in extract_xml_data(zip_file):
        variable_rows.append([xml_data.xml_id, xml_data.level])
        object_rows += [
            [xml_data.xml_id, name]
            for name in xml_data.object_names
        ]

    variables_csv.write_rows(variable_rows)
    objects_csv.write_rows(object_rows)


class ReportGenerator:
    def __init__(
        self,
        variables_report_filename='variables_report.csv',
        objects_report_filename='objects_report.csv',
    ):
        self._variables_csv = СSVWriter(variables_report_filename)
        self._objects_csv = СSVWriter(objects_report_filename)
        self._proceed_zip_file = partial(
            proceed_zip_file,
            variables_report_filename=variables_report_filename,
            objects_report_filename=objects_report_filename,
        )

    def generate(self, data_path: Path, max_workers=16):
        self._variables_csv.write_header(columns=['id', 'level'])
        self._objects_csv.write_header(columns=['id', 'object_name'])

        executor = ThreadPoolExecutor(max_workers=max_workers)
        zip_files = (file for file in data_path.iterdir() if file.is_file())
        executor.map(self._proceed_zip_file, zip_files)


if __name__ == '__main__':
    path = Path('../data')
    report_generator = ReportGenerator()
    print(timeit.timeit(lambda: report_generator.generate(path), number=100))
