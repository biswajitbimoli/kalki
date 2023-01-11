import os
import kalki.settings as settings
import sys
from kalki import service
try:
    from kalki import kalkiminify
except:
    pass
# try:
#     from kalki import service
# except:
#     pass
try:
    from kalki import create_app
except:
    pass


path = settings.kalki_path



try:
    appname = sys.argv[2]
except:
    print('provide a appname')
def check_appname():
    for app in settings.APP_NAME:
        if app == appname:
            return True


def startapp():
    create_app.startapp(appname)

def compile():
    if check_appname():
        service.service(appname)
    else:
        print('Appname do not exists.')
        print("If the app exists, add the app to APP_NAME in settings.py")
    

def minify():
    if check_appname():
        kalkiminify.kalkiminify(appname)
    else:
        print('Appname do not exists.')
        print("If the app exists, add the app to APP_NAME in settings.py")

if __name__ == '__main__':
    try:
        globals()[sys.argv[1]]()
    except IndexError:
        print("""
            available commands-
                startapp
                compile
                minify
            Use these commands like-
                'python kalki.py startapp' to create working directory
                'python kalki.py compile' to create compiled css file
                'python kalki.py minify' to create minified css file
            """)