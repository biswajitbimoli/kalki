import os
import sys
import kalki.settings as settings


class StartApp:
    def __init__(self, appname):
        self.path = settings.styles_path
        self.appname = appname + '.kalki'

    def create_kalki_file(self):
        try:
            os.mkdir(self.path)
        except FileExistsError:
            print("Directory 'styles' already created.")
            print("Trying to create required files")
        file_name = os.path.join(self.path, self.appname)
        
        try:
            create_kalki_file = open(file_name, 'x')
        except FileExistsError:
            print(f"App {file_name} already exists.")
            sys.exit()
        kalki_content = """@kalki
@global

colors = ['red', 'green', 'blue', 'purple', 'orange', 'black']

@endkalki


* {
    padding: auto;
}

@kalki
for color in colors:
  @css
  .bg-{color} {{
    background-color: {color};
  }}
  @endcss
for color in colors:
  @css
  .text-{color} {{
    color: {color};
  }}
  @endcss
@endkalki
"""
        create_kalki_file.write(kalki_content)
        create_kalki_file.close()
        print(f"{self.appname} file created successfully in 'styles' subdirectory inside the main app")