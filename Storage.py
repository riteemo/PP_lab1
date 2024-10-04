from HospitalInhabitant import *

# класс "хранилище"
class Storage:
    def __init__(self):
        self.storage = {
            "cleaners": [],
            "doctors": [],
            "guards": [],
            "nurses": [],
            "patients": [],
            "visitors": []
        }

    # добавление записи
    def add(self, key: str, data: HospitalInhabitant) -> None:
        try:
            self.storage[key].append(data)
        except KeyError:
            print("No such key in storage")

    # обновление записи
    def update(self, key: str, index: int, new: HospitalInhabitant) -> None:
        try:
            self.storage[key][index] = new
        except KeyError:
            print("No such key in storage")
        except IndexError:
            print("List index out of range")

    # добавление записей
    def extend(self, key: str, data: list[HospitalInhabitant]) -> None:
        try:
            self.storage[key].extend(data)
        except KeyError:
            print("No such key in storage")

    # получение записей
    def get_all_of(self, key: str) -> list[HospitalInhabitant]:
        try:
            return self.storage[key]
        except KeyError:
            print("No such key in storage")

    # удаление записи
    def delete(self, key: str) -> HospitalInhabitant:
        try:
            return self.storage[key].pop()
        except KeyError:
            print("No such key in storage")

