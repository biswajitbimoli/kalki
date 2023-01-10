import os
import kalki.settings as settings
import sys
from kalki import service, kalkiminify
path = settings.kalki_path


def startapp():
    exec(open(os.path.join(path, "startapp.py")).read())

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