import os
import re
import sys
import kalki.settings as settings
from kalki.minify import minify_logic as ml

class Minify:
    def __init__(self, appname):
        self.appname = appname + '-compiled.min.css'
        self.css_filename = appname + '-compiled.css'
        self.output_path = settings.output_path
        self.content = ''
        self.kalkicss = ''

    def read_css(self):
        try:
            file = open(os.path.join(self.output_path, self.css_filename))
            self.content = file.read()
            file.close()
        except FileNotFoundError:
            print(f'{self.css_filename} do not exists.')
            print(f"Run compile {self.appname} to create {self.css_filename}")
            sys.exit()

    def remove_spaces(self):
        self.kalkicss = ml.MinifyLogic(self.content).minify_file()
        self.kalkicss += '\n/*created using kalki*/'

    def create_min_css(self):
        created_css = open(os.path.join(self.output_path, self.appname), 'w')
        created_css.write(self.kalkicss)
        created_css.close()
        print(f"{self.appname} file created successfully in 'output' subdirectory inside the main app")

    # executes all minify functions
    def minify(self):
        self.read_css()
        self.remove_spaces()
        self.create_min_css()