import os

BASE_DIR = os.getcwd()
kalki_path = os.path.join(BASE_DIR, 'output')
file = open(os.path.join(kalki_path, 'kalki.css'))
content = file.read()
file.close()

kalkicss = ""
new = content.replace(' ', '')
new = new.split();
for i in new:
    kalkicss += i

created_css = open(os.path.join(kalki_path, 'kalki.min.css'), 'w')
created_css.write(kalkicss)
created_css.close()
print("kalki.min.css file created successfully")