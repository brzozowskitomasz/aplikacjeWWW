class FileManager():
    def __init__(self,file_name):
        self.file_name = file_name
    def read_file(self):
        try:
            uchwyt = open(self.file_name,"r")
            wynik = uchwyt.read()
            uchwyt.close()
            return wynik
        except FileNotFoundError as e:
            print("Plik o podanej nazwie nie istnieje")
            print(e)

    def update_file(self, text_data):
        uchwyt = open(self.file_name,"a+")
        uchwyt.write(text_data)
        uchwyt.close







