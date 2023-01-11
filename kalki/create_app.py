from kalki.startapps import main
import os

def startapp(appname):
    base = os.getcwd()
    path = os.path.join(base, 'kalki/settings.py')
    if not os. path.isfile(path):
        main.StartApp(appname).create_settings()
        print("settings.py created successfully")
    main.StartApp(appname).create_kalki_file()