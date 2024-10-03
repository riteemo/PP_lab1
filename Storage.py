from HospitalInhabitant import *

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

    def update(self, key: str, data: HospitalInhabitant) -> None:
        self.storage[key].append(data) #DOBAVIT VALIDACIY PO PARAMETRY KEY

    def extend(self, key: str, data: list[HospitalInhabitant]) -> None:
        self.storage[key].extend(data)

    def get_all_of(self, key: str) -> list[HospitalInhabitant]:
        return self.storage[key]

    def delete(self, key: str) -> HospitalInhabitant:
        return self.storage[key].pop()

