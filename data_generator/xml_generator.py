from collections.abc import Iterator
from dataclasses import dataclass
from random import randint
from uuid import UUID
from uuid import uuid4
from xml.etree import ElementTree


@dataclass(frozen=True)
class ValueRange:
    start: int
    end: int


class XMLFileGenerator(Iterator):
    def __init__(self, files_count: int, level_range: ValueRange, objects_range: ValueRange):
        self.__level_range = level_range
        self.__objects_range = objects_range
        self.__files = self.__generate_files(files_count)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.__files)

    def __generate_files(self, n):
        for _ in range(n):
            level = randint(self.__level_range.start, self.__level_range.end)
            objects_count = randint(self.__objects_range.start, self.__objects_range.end)
            xml_tree = create_xml(level=level, children_count=objects_count)
            yield ElementTree.tostring(xml_tree, method='xml')


def create_xml(level: int, children_count: int, id_: UUID = None) -> ElementTree:
    root = ElementTree.Element('root')
    xml_id = id_ or uuid4()
    ElementTree.SubElement(root, 'var', attrib={'name': 'id', 'value': str(xml_id)})
    ElementTree.SubElement(root, 'level', attrib={'name': 'level', 'value': str(level)})

    objects = ElementTree.SubElement(root, 'objects')
    for _ in range(children_count):
        ElementTree.SubElement(objects, 'object', attrib={'name': str(uuid4())})

    return root
