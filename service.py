file = open('kalki.pycss')
content = file.read()
file.close()

list_content = content.split('@kalki')

kalkicss = ""

for i in list_content:
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

created_css = open('styles/kalki.css', 'w')
created_css.write(kalkicss)
created_css.close()
exec(open("kalkiminify.py").read())