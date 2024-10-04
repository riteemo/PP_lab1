from HospitalInhabitant import HospitalInhabitant

# дочерний класс "уборщик"
class Cleaner(HospitalInhabitant):
    def __init__(self, name: str, surname: str, phone: str, floor : int):
        super().__init__(name, surname, phone)
        self.floor = floor
