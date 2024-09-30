from HospitalInhabitant import HospitalInhabitant

class Receptionist(HospitalInhabitant):
    def __init__(self, name: str, surname: str, phone: str, work_id: int):
        super().__init__(name, surname, phone)
        self.work_id = work_id
