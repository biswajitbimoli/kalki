import kalki.settings as settings
import os
import sys
import re


class Compile:
    def __init__(self):
        self.styles_path = settings.styles_path
        self.output_path = settings.output_path
        self.kalki_path = settings.kalki_path
        self.kalki_content = ''
        self.kalki_list_content = ''
        self.kalkicss = ""
        self.kalki_global = ''

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

        self.kalki_global = ''

        for i in self.kalki_list_content:
            a = i.strip()
            if a.startswith('@global'):
                a = a.replace('@global', '')
                kalki_global = a
                self.kalki_list_content.remove(i)


    def create_kalki_css(self):

        for i in self.kalki_list_content:
            a = len(i.split('@css'))
            if a > 1:
                code = i.replace('@css', 'style = f"""')
                code = code.replace('@endcss', '"""; @endcss')
                code = code.replace('${', '{{')
                code = code.replace('}$', '}}')
                code = code.replace('@endcss', "css.append(style)")
                css = []
                css_all = ""
                code_exec = exec(code)
                for l in css:
                    s = l.strip()
                    css_all += '\n' + s
                    i = css_all
            else:
                i = i.replace('#', '/*')
                i = i.replace('$', '*/')
            self.kalkicss += i;
        self.kalkicss = self.kalkicss.replace(' ', '')
        self.kalkicss = re.sub(r'\n\s*\n','\n',self.kalkicss,re.MULTILINE)
    
    def write_css_file(self):
        try:
            os.mkdir(self.output_path)
        except FileExistsError:
            print("Directory 'output' already created.")
            print("Trying to create compiled css files")

        kalki_created_css = open(os.path.join(self.output_path, settings.dot_css), 'w')
        kalki_created_css.write(self.kalkicss)
        kalki_created_css.close()
        print(f"{settings.dot_css} file created successfully in 'output' subdirectory inside the main app")

    def compile(self):
        self.open_kalki_file()
        self.check_kalki_syntax()
        self.exec_kalki_global()
        exec(self.kalki_global)
        self.create_kalki_css()
        self.write_css_file()

