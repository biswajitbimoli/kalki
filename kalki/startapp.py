import os
import sys
import kalki.settings as settings

path = settings.styles_path

try:
    os.mkdir(path)
except FileExistsError:
    print("Directory 'styles' already created.")
    print("Trying to create required files")
file_name = os.path.join(path, settings.dot_kalki)
if os.path.exists(file_name):
  print('working directory and required file is already created')
  sys.exit()
  
create_kalki_file = open(file_name, 'w')
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
print(f"{settings.dot_kalki} file created successfully in 'styles' subdirectory inside the main app")