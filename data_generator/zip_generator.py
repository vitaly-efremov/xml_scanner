import zipfile
from pathlib import Path
from typing import Iterator

from data_generator.xml_generator import ValueRange
from data_generator.xml_generator import XMLFileGenerator


def archive_files(zip_name: str, files: Iterator):
    with zipfile.ZipFile(zip_name, mode='w') as archive:
        for file_number, xml in enumerate(files):
            archive.writestr(f'{file_number}.xml', xml)


def generate_data(
    zip_files_count: int = 50,
    xml_files_count: int = 100,
    level_value_range: ValueRange = ValueRange(1, 100),
    objects_value_range: ValueRange = ValueRange(1, 10),
    path: Path = Path('data'),
):
    for index in range(zip_files_count):
        xml_files = XMLFileGenerator(xml_files_count, level_range=level_value_range, objects_range=objects_value_range)
        file_path = path.joinpath(f'{index}.zip')
        archive_files(zip_name=str(file_path), files=xml_files)
