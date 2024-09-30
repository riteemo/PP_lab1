from Cleaner import *
from Doctor import *
from Guard import *
from HospitalInhabitant import *
from Nurse import *
from Patient import *
from Visitor import *

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

    def update(self, key: str, data: HospitalInhabitant):
        self.storage[key].append(data)

