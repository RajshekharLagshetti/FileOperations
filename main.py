# This code is for file operations like read, write, download, etc
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


import logging as lg
import json

class data:
    def __init__(self, filename, filetype):
        self.filename = filename
        self.filetype = filetype

    def filewrite(self, dict):
        f = open(self.filename + '.' + self.filetype, 'w')
        f.write(dict)
        f.close()

    def fileread(self):
        try:
            if self.filetype == "txt":
                f = open(self.filename + '.' + self.filetype, 'r')
                for i in f:
                    print(i)
                f.close()
            else:
                f = open(self.filename + '.' + self.filetype, 'r')
                js = json.load(f)
                print(js["name"])
        except Exception as e:
            self.logging(e)
            print("Error type:", e)

    def fileappend(self, dict):
        f = open(self.filename + '.' + self.filetype, 'a')
        f.write(dict)
        f.close()

    def logging(self, log):
        lg.basicConfig(filename="logfile.log", format="%(asctime)s %(message)s", level=lg.INFO)
        lg.error("error has occured")
        lg.exception(str(log))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    s = """{
    "name" : "raj",
    "phone_no": 90757981212,
    "company":["HAL", "BHEL", "BEL", "ISRO", "DRDO"]
    }
    """
    filereadwrite = data("test1", "json")
    filereadwrite.filewrite(s)
    filereadwrite.fileread()

