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

count1 = kalki_content.count('@kalki')
count2 = kalki_content.count('@endkalki')

if count1 != count2:
    if count1 > count2:
        print("You might have left a @kalki tag openned, please close it with @endkalki to compile the code")
    else:
        print("You might have extra @endkalki tag, please remove it to compile the code")
    sys.exit()
if kalki_content.count('@global') > 1:
    print("You have added @global keyword twice, you can use only one @global keyword")
    sys.exit()

kalki_list_content = re.split(r'@kalki|@endkalki', kalki_content)

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
        code = i.replace('@css', 'style = f"""')
        code = code.replace('@endcss', '"""; @endcss')
        code = code.replace('${', '{{')
        code = code.replace('}$', '}}')
        code = code.replace('@endcss', "css.append(style)")
        css = []
        css_all = ""
        code_exec = exec(code)
        for l in css:
            s = l.strip()
            css_all += '\n' + s
            i = css_all
    else:
        i = i.replace('#', '/*')
        i = i.replace('$', '*/')
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
print(f"{settings.dot_css} file created successfully in 'output' subdirectory inside the main app")
exec(open(os.path.join(kalki_path, "kalkiminify.py")).read())

