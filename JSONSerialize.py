from json import dump, load

class JSONSerialize:
    def read(self, path: str) -> dict:
        with open(path) as json_input:
            return load(json_input)

    def write(self, path: str, data: dict) -> None:
        with open(path, "w") as json_output:
            dump(data, json_output)