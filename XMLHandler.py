from xml_marshaller import xml_marshaller
from dicttoxml import dicttoxml

class XMLHandler:
    def read(self, path: str) -> dict:
        with open(path) as xml_input:
            data = xml_marshaller.load(xml_input)
            return data

    def write(self, path: str, data: dict) -> None:
        new_data = data.copy()
        for key in data:
            new_data[key] = list(map(lambda x: x.__dict__, new_data[key]))
        out = dicttoxml(new_data, attr_type=False)
        with open(path, "wb") as xml_output:
            xml_output.write(out)



