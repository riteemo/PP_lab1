from HospitalInhabitant import HospitalInhabitant

# дочерний класс "посетитель"
class Visitor(HospitalInhabitant):
    def __init__(self, name: str, surname: str, phone: str, patient_id: int):
        super().__init__(name, surname, phone)
        self.patient_id = patient_id
