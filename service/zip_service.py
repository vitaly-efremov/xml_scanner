from pathlib import Path
from xml.etree import ElementTree
from zipfile import ZipFile


def read_zip(file_path: Path):
    with ZipFile(file_path) as zip_file:
        for xml_file in zip_file.filelist:
            with zip_file.open(xml_file.filename) as xml_file:
                yield ElementTree.parse(xml_file)

