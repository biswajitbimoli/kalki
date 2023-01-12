import kalki.settings as settings
import os
import sys
import re
from kalki.services import global_var

exec(global_var.kalki_global)

class Compile(global_var.GlobalVar):


    def create_kalki_css(self):
        
        kalki_css = ''

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
                exec(code)
                for l in css:
                    # s = l.strip()
                    css_all += '\n' + l
                    i = css_all

            kalki_css += i;
        k_c = re.findall(r'.+', kalki_css)
        for i in k_c:
            l = i.strip()
            if l != '':
                self.kalkicss += '\n' + l
        self.kalkicss = re.sub(r'\#.+','', self.kalkicss, re.MULTILINE)
        self.kalkicss = re.sub(r'\n\s*\n','\n',self.kalkicss,re.MULTILINE)
        
    
    def write_css_file(self):
        try:
            os.mkdir(self.output_path)
        except FileExistsError:
            print("Directory 'output' already created.")
            print("Trying to create compiled css files")

        kalki_created_css = open(os.path.join(self.output_path, self.css_filename), 'w')
        kalki_created_css.write(self.kalkicss)
        kalki_created_css.close()
        print(f"{self.css_filename} file created successfully in 'output' subdirectory inside the main app")

    def compile(self):
        self.exec_kalki_global()
        self.create_kalki_css()
        self.write_css_file()

