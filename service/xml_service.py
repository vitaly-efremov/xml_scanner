from dataclasses import dataclass
from typing import Generator
from typing import Iterable

from service.zip_service import read_zip


@dataclass(frozen=True)
class XMLData:
    xml_id: str
    level: str
    object_names: Iterable[str]


def extract_xml_data(zip_file) -> Generator[XMLData, None, None]:
    for xml_root in read_zip(zip_file):
        variables = {tag.attrib['name']: tag.attrib['value'] for tag in xml_root.findall('./var')}
        object_names = (tag.attrib['name'] for tag in xml_root.findall('./objects/object'))
        yield XMLData(
            xml_id=variables['id'],
            level=variables['level'],
            object_names=object_names,
        )
