import os
import kalki.settings as settings
import sys
try:
    from kalki import kalkiminify
except:
    pass
try:
    from kalki import service
except:
    pass
try:
    from kalki import create_app
except:
    pass


path = settings.kalki_path


def startapp():
    create_app.startapp()

def compile():
    service.service()

def minify():
    kalkiminify.kalkiminify()

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