from HospitalInhabitant import HospitalInhabitant

# дочерний класс "медсестра"
class Nurse(HospitalInhabitant):
    def __init__(self, name: str, surname: str, phone: str, experience : int):
        super().__init__(name, surname, phone)
        self.experience = experience
