import os
import sys


class StartApp:
    def __init__(self, appname):
        self.BASE_DIR = os.getcwd()
        if os.path.isfile(os.path.join(self.BASE_DIR, 'settings.py')):
            import settings
            self.styles_path = settings.styles_path
        else:
            self.styles_path = os.path.join(self.BASE_DIR, 'styles')
        self.appname = appname + '.kalki'
        self.app = appname

    def create_settings(self):
        file_name = os.path.join(self.BASE_DIR, 'settings.py')
        try:
            create_settings_file = open(file_name, 'x')
            settings_content = f"""import os

BASE_DIR = os.getcwd()
kalki_path = os.path.join(BASE_DIR, 'kalki')
styles_path = os.path.join(BASE_DIR, 'styles')
output_path = os.path.join(BASE_DIR, 'output')

# .kalki file name
dot_css = 'kalki-compiled.css'
dot_min_css = 'kalki-compiled.min.css'

APP_NAME = [
    '{self.app}'
]"""
            create_settings_file.write(settings_content)
            create_settings_file.close()
        except FileExistsError:
            print(f"App {file_name} already exists.")
            pass


    def create_kalki_file(self):
        try:
            os.mkdir(self.styles_path)
        except FileExistsError:
            print("Directory 'styles' already created.")
            print("Trying to create required files")
        file_name = os.path.join(self.styles_path, self.appname)

        try:
            create_kalki_file = open(file_name, 'x')
        except FileExistsError:
            print(f"App {file_name} already exists.")
            sys.exit()
        kalki_content = """@kalki_global

colors = ['red', 'green', 'blue', 'purple', 'orange', 'black']

@endkalki


* {
    padding: auto;
}

@kalki
for color in colors:
    @css
    .bg-{{color}} {
        background-color: {{color}};
    }
    @endcss
for color in colors:
    @css
    .text-{{color}} {
        color: {{color}};
    }
    @endcss
@endkalki
"""
        create_kalki_file.write(kalki_content)
        create_kalki_file.close()
        print(
            f"{self.appname} file created successfully in 'styles' subdirectory inside the main app")
