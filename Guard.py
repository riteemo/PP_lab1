from HospitalInhabitant import HospitalInhabitant

# дочерний класс "охранник"
class Guard(HospitalInhabitant):
    def __init__(self, name: str, surname: str, phone: str, weapon: str):
        super().__init__(name, surname, phone)
        self.weapon = weapon
