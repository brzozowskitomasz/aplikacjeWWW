from file_manager import *
f_m = FileManager("plik_testowy.txt")
f_m.update_file("Lorem Ipsum")
print(f_m.read_file())
