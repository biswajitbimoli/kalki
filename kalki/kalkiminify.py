import os
import kalki.settings as settings

output_path = settings.output_path
file = open(os.path.join(output_path, 'kalki.css'))
content = file.read()
file.close()

kalkicss = ""
new = content.replace(' ', '')
new = new.split();
for i in new:
    kalkicss += i

created_css = open(os.path.join(output_path, 'kalki.min.css'), 'w')
created_css.write(kalkicss)
created_css.close()
print("kalki.min.css file created successfully")