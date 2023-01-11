from kalki.services import compile, global_var
from kalki import kalkiminify

def service(appname):
    compile.Compile(appname).compile()
    kalkiminify.kalkiminify(appname)

