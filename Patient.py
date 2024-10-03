from HospitalInhabitant import HospitalInhabitant

class Patient(HospitalInhabitant):
    def __init__(self, name: str, surname: str, phone: str, id : int, diagnosis : str):
        super().__init__(name, surname, phone)
        self.id = id
        self.diagnosis = diagnosis