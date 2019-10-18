class file_manager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        file=open(self.file_name,'r')
        print(file.read())

    def update_file(self, text_data):
        file=open(self.file_name,'a')
        file.write("\n"+text_data)
        file.close()


obiekt=file_manager("cos.txt")
obiekt.read_file()
obiekt.update_file("cooos")
obiekt.read_file()


