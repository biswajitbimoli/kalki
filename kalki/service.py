import os
import re
import sys
import kalki.settings as settings

styles_path = settings.styles_path
output_path = settings.output_path
kalki_path = settings.kalki_path

file = open(os.path.join(styles_path, settings.dot_kalki))
kalki_content = file.read()
file.close()

count = kalki_content.count('@kalki')

if count%2 != 0:
    print("You might have left a @kalki tag openned, please close it to compile the code")
    sys.exit()

kalki_list_content = kalki_content.split('@kalki')

kalki_global = ''

for i in kalki_list_content:
    a = i.strip()
    if a.startswith('@global'):
        a = a.replace('@global', '')
        kalki_global = a
        kalki_list_content.remove(i)
    

exec(kalki_global)

kalkicss = ""

for i in kalki_list_content:
    a = len(i.split('@css'))
    if a > 1:
        code = i.replace('@css', 'f"""')
        code = code.replace('@end', '"""')
        code = code.replace('${', '{{')
        code = code.replace('}$', '}}')
        code = code.replace('@addkalki', "css.append(style)")
        css = []
        css_all = ""
        code_exec = exec(code)
        for l in css:
            s = l.strip()
            css_all += '\n' + s
            i = css_all
    kalkicss += i;
kalkicss = kalkicss.replace(' ', '')
kalkicss = re.sub(r'\n\s*\n','\n',kalkicss,re.MULTILINE)

try:
    os.mkdir(output_path)
except FileExistsError:
    print("Directory 'output' already created.")
    print("Trying to create compiled css files")

kalki_created_css = open(os.path.join(output_path, settings.dot_css), 'w')
kalki_created_css.write(kalkicss)
kalki_created_css.close()
print('kalki.css file created successfully')
exec(open(os.path.join(kalki_path, "kalkiminify.py")).read())

