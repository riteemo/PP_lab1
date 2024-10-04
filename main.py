from JSONHandler import *
from XMLHandler import *
from Storage import *
from Cleaner import *
from Doctor import *
from Guard import *
from Nurse import *
from Patient import *
from Visitor import *


storage = Storage() # объект хранилища
json_file = JSONHandler() # обработчик для JSON'a
xml_file = XMLHandler() # обработчик для XML'a

# стандартные данные
keys = {
   "cleaners": [Cleaner("Antonia", "Harley", "+7(4212)68-49-54", 1), Cleaner("Luanna", "Colter", "+7(3519)82-82-96", 2)],
   "doctors": [Doctor("Freddy", "Biff", "+7(495)153-76-62", "Pediatrician" ), Doctor("Ashton", "Malaysia", "+7(4212)58-16-40", "Dentist")],
   "guards": [Guard("Austen", "Fisher", "+7(843)541-84-48", "Handgun"), Guard("Ormond", "Quincy", "+7(8652)71-65-15", "Revolver")],
   "nurses": [Nurse("Chyna", "French", "+7(347)555-34-66", 1), Nurse("Marylou", "Barker", "+7(8452)92-87-60", 2)],
   "patients": [Patient("Scotty", "Haden", "+7(4922)59-59-08", 1, "Cholera"), Patient("Brenton", "James", "+7(3519)34-08-03", 2, "Gonorrhea")],
   "visitors": [Visitor("Walton", "Paternoster", "+7(3519)34-99-49", 1), Visitor("Cate", "Foss", "+7(831)522-42-79", 2)]
}

# заполнение хранилища
for key in keys:
   storage.extend(key, keys[key])

# обновление хранилища
storage.add("doctors", Doctor("Anna", "Cringe", "+7(919)34-92-79", "Eye doctor"))
storage.update("doctors", 2, Doctor("Anna", "Slay", "+7(919)34-92-79", "Eye doctor"))

# сериализация и десериализация JSON
json_file.write("test.json", storage.storage)
json_result = json_file.read("test.json")
print(f"JSON: {json_result}")

# сериализация и десериализация XML
xml_file.write("test.xml", storage.storage)
xml_result = xml_file.read("test.xml")
print(f"XML: {xml_result}")