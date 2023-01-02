import os

BASE_DIR = os.getcwd()

kalki_path = os.path.join(BASE_DIR, 'styles')

try:
    os.mkdir(kalki_path)
except FileExistsError:
    print("Directory 'styles' already created.")
    print("Trying to create required files")

create_kalki_file = open(os.path.join(kalki_path, 'kalki.kalki'), 'w')
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