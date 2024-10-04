# родительский класс "обитатель больницы"
class HospitalInhabitant:
    def __init__(self, name: str, surname: str, phone: str):
        self.name = name
        self.surname = surname
        self.phone = phone