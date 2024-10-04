import xml.etree.ElementTree as ET
from dicttoxml import dicttoxml
from xmltodict import parse

# класс для сериализации и десериализации xml
class XMLHandler:
    def read(self, path: str) -> dict:
        try:
            with open(path) as xml_input:
                return parse(xml_input.read())
        except Exception():
            print("Read error occured")

    def write(self, path: str, data: dict) -> None:
        try:
            new_data = data.copy()
            for key in data:
                new_data[key] = list(map(lambda x: x.__dict__, new_data[key]))
            out = dicttoxml(new_data, attr_type=False)
            with open(path, "wb") as xml_output:
                xml_output.write(out)
        except Exception():
            print("Write error occured")



