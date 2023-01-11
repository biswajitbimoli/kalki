from kalki.services import compile, global_var
from kalki import kalkiminify

def service():
    compile.Compile().compile()
    kalkiminify.kalkiminify()

