import os

BASE_DIR = os.getcwd()

file = open(os.path.join(BASE_DIR, 'styles/kalki.kalki'))
kalki_content = file.read()
file.close()

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


kalki_path = os.path.join(BASE_DIR, 'output')

try:
    os.mkdir(kalki_path)
except FileExistsError:
    print("Directory 'output' already created.")
    print("Trying to create compiled css files")

kalki_created_css = open(os.path.join(kalki_path, 'kalki.css'), 'w')
kalki_created_css.write(kalkicss)
kalki_created_css.close()
exec(open("kalkiminify.py").read())

print('kalki.css and kalki.min.css files created successfully')