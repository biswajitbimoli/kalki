file = open('styles/kalki.css')
content = file.read()
file.close()

kalkicss = ""
new = content.replace(' ', '')
new = new.split();
for i in new:
    kalkicss += i

created_css = open('styles/kalki.min.css', 'w')
created_css.write(kalkicss)
created_css.close()