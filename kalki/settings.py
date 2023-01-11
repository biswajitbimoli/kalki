import os

BASE_DIR = os.getcwd()
kalki_path = os.path.join(BASE_DIR, 'kalki')
styles_path = os.path.join(BASE_DIR, 'styles')
output_path = os.path.join(BASE_DIR, 'output')

# .kalki file name
dot_css = 'kalki-compiled.css'
dot_min_css = 'kalki-compiled.min.css'

APP_NAME = [
    'app',
    'newfile',
]