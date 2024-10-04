from HospitalInhabitant import HospitalInhabitant

# дочерний класс "доктор"
class Doctor(HospitalInhabitant):
    def __init__(self, name: str, surname: str, phone: str, specialty: str):
        super().__init__(name, surname, phone)
        self.specialty = specialty


