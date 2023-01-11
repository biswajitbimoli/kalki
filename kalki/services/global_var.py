import kalki.settings as settings
import os
import sys
import re

kalki_global = ''

class GlobalVar:
    def __init__(self):
        self.styles_path = settings.styles_path
        self.output_path = settings.output_path
        self.kalki_path = settings.kalki_path
        self.kalki_content = ''
        self.kalki_list_content = ''
        self.kalkicss = ""

    def open_kalki_file(self):
        file = open(os.path.join(self.styles_path, settings.dot_kalki))
        self.kalki_content = file.read()
        file.close()
        self.kalki_list_content = re.split(r'@kalki|@endkalki', self.kalki_content)

    def check_kalki_syntax(self):
        count1 = self.kalki_content.count('@kalki')
        count2 = self.kalki_content.count('@endkalki')
        if count1 != count2:
            if count1 > count2:
                print("You might have left a @kalki tag openned, please close it with @endkalki to compile the code")
            else:
                print("You might have extra @endkalki tag, please remove it to compile the code")
            sys.exit()
        if self.kalki_content.count('@global') > 1:
            print("You have added @global keyword twice, you can use only one @global keyword")
            sys.exit()

    def exec_kalki_global(self):
        self.open_kalki_file()
        self.check_kalki_syntax()
        global kalki_global
        kalki_global = ''

        for i in self.kalki_list_content:
            a = i.strip()
            if a.startswith('@global'):
                a = a.replace('@global', '')
                kalki_global = a
                self.kalki_list_content.remove(i)
        
        
        # file = open(os.path.join(self.kalki_path, 'kalki_global.py'), mode='w')
        # file.write(kalki_global)
        # file.close()
GlobalVar().exec_kalki_global()