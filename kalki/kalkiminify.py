import os
import re
import kalki.settings as settings

output_path = settings.output_path
file = open(os.path.join(output_path, settings.dot_css))
content = file.read()
file.close()

kalkicss = ""
new = content.replace(' ', '')
# new = re.sub(r'^/\*.\*/$', '', new)
new = new.split();
for i in new:
    kalkicss += i

created_css = open(os.path.join(output_path, settings.dot_min_css), 'w')
created_css.write(kalkicss)
created_css.close()
print(f"{settings.dot_min_css} file created successfully in 'output' subdirectory inside the main app")