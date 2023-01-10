from kalki.services.compile import Compile
from kalki import kalkiminify

def service():
    Compile().compile()
    kalkiminify.kalkiminify()

