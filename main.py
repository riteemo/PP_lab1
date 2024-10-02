from JSONSerialize import *

test = JSONSerialize()
print(type(test.read(r"C:\Users\irina\OneDrive\Desktop\json_test.json")))

dct = {
   "key" : "data"
}
test.write("test.json", dct)