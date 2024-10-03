from json import dump, load

class JSONHandler:
    def read(self, path: str) -> dict:
        with open(path) as json_input:
            return load(json_input)

    def write(self, path: str, data: dict) -> None:
        new_data = data.copy()
        for key in data:
            new_data[key] = list(map(lambda x: x.__dict__, new_data[key]))
        with open(path, "w") as json_output:
            dump(new_data, json_output)

