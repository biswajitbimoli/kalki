import os
import re
import kalki.settings as settings

class Minify:
    def __init__(self):
        self.output_path = settings.output_path
        self.content = ''
        self.kalkicss = ''

    def read_css(self):
        file = open(os.path.join(self.output_path, settings.dot_css))
        self.content = file.read()
        file.close()

    def remove_spaces(self):
        new = self.content.replace(' ', '')
        # new = re.sub(r'^/\*.\*/$', '', new)
        new = new.split();
        for i in new:
            self.kalkicss += i
        self.kalkicss += '\n/*created using kalki*/'

    def create_min_css(self):
        created_css = open(os.path.join(self.output_path, settings.dot_min_css), 'w')
        created_css.write(self.kalkicss)
        created_css.close()
        print(f"{settings.dot_min_css} file created successfully in 'output' subdirectory inside the main app")

    # executes all minify functions
    def minify(self):
        self.read_css()
        self.remove_spaces()
        self.create_min_css()