from pathlib import Path
from typing import Generator
from xml.etree import ElementTree
from zipfile import ZipFile


def read_zip(file_path: Path) -> Generator[ElementTree.ElementTree, None, None]:
    with ZipFile(file_path) as zip_file:
        for file in zip_file.filelist:
            with zip_file.open(file.filename) as xml_file:
                yield ElementTree.parse(xml_file)

