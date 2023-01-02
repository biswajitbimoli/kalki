import os
import kalki.settings as settings

path = settings.styles_path

try:
    os.mkdir(path)
except FileExistsError:
    print("Directory 'styles' already created.")
    print("Trying to create required files")

create_kalki_file = open(os.path.join(path, settings.dot_kalki), 'w')
kalki_content = """@kalki
@global

colors = ['red', 'green', 'blue', 'purple', 'orange', 'black']

@kalki


* {
    padding: auto;
}

@kalki
for color in colors:
  style = @css
  .bg-{color} ${
    background-color: {color};
  }$
  @end
  @addkalki
for color in colors:
  style = @css
  .text-{color} ${
    color: {color};
  }$
  @end
  @addkalki
@kalki
"""
create_kalki_file.write(kalki_content)
create_kalki_file.close()
print('kalki.kalki file created successfully')